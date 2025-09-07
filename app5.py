import gradio as gr
import pandas as pd

# Load dataset
df = pd.read_csv("C:/AI workforce/clustering/Customer_Segments.csv")

# ---------------------------
# Helper functions
# ---------------------------
def get_dataset_head():
    return df.head()

def get_cluster_profile():
    cluster_profile = df.groupby("Cluster").agg({
        "Recency": "mean",
        "Frequency": "mean",
        "Monetary": "mean",
        "CustomerID": "count"
    }).rename(columns={"CustomerID": "NumCustomers"})
    return cluster_profile

def predict_cluster(customer_id):
    try:
        customer_id = int(customer_id)
    except:
        return "⚠️ Please enter a valid numeric CustomerID."

    if customer_id in df["CustomerID"].values:
        row = df.loc[df["CustomerID"] == customer_id]
        cluster = row["Cluster"].values[0]
        segment = row["Segment"].values[0]
        return f"✅ Customer **{customer_id}** belongs to **Cluster {cluster} ({segment})**"
    else:
        return "⚠️ Customer ID not found in dataset."

# ---------------------------
# Login Functionality
# ---------------------------
def login(username, password):
    if username == "admin" and password == "1234":
        return "dashboard", "✅ Login successful! Welcome 🎉"
    else:
        return "login", "❌ Invalid credentials. Try again."

# ---------------------------
# Gradio Interface
# ---------------------------
with gr.Blocks(
    css="""
    .card {
        background-color: white;
        border-radius: 12px;
        padding: 25px;
        margin: 20px 0;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    }
    """
) as demo:
    screen = gr.State("login")  # keep track of current screen

    # Login Screen
    with gr.Group(visible=True) as login_screen:
        gr.Markdown("<h1 style='text-align:center; color:#2E86C1'>🛍️ Customer Segmentation App</h1>")
        gr.Markdown("### Please log in to continue")

        username = gr.Textbox(label="Username", placeholder="Enter username")
        next_btn = gr.Button("➡️ Next")

        password = gr.Textbox(label="Password", placeholder="Enter password", type="password", visible=False)
        login_btn = gr.Button("🔓 Login", visible=False)
        login_msg = gr.Markdown("")

        # Step-by-step login reveal
        def show_password(u):
            if u.strip() == "":
                return gr.update(visible=False), gr.update(visible=False), "⚠️ Please enter a username first."
            else:
                return gr.update(visible=True), gr.update(visible=True), ""
        
        next_btn.click(show_password, inputs=username, outputs=[password, login_btn, login_msg])

    # Dashboard Screen
    with gr.Group(visible=False) as dashboard_screen:
        gr.Markdown("<h2 style='color:#117864; text-align:center;'>📊 Customer Dashboard</h2>")

        with gr.Column(elem_classes="card"):
            gr.Markdown("### 📂 Dataset Preview")
            dataset_out = gr.Dataframe(value=get_dataset_head(), wrap=True)

        with gr.Column(elem_classes="card"):
            gr.Markdown("### 🔎 Cluster Profiling")
            profile_out = gr.Dataframe(value=get_cluster_profile(), wrap=True)

        with gr.Column(elem_classes="card"):
            gr.Markdown("### 🎯 Predict Cluster for a Customer")
            customer_id = gr.Textbox(label="Enter CustomerID")
            predict_btn = gr.Button("Predict Cluster")
            predict_out = gr.Markdown()
            predict_btn.click(fn=predict_cluster, inputs=customer_id, outputs=predict_out)

    # Switch screens based on login result
    def handle_login(u, p):
        scr, msg = login(u, p)
        if scr == "dashboard":
            return gr.update(visible=False), gr.update(visible=True), msg
        else:
            return gr.update(visible=True), gr.update(visible=False), msg

    login_btn.click(handle_login, inputs=[username, password], outputs=[login_screen, dashboard_screen, login_msg])

# ---------------------------
# Launch
# ---------------------------
demo.launch()
