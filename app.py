import streamlit as st

# Tiêu đề ứng dụng
st.title("💰 Ứng dụng tính Thuế Thu nhập cá nhân của Thảo Ly")

# Nhập dữ liệu
thu_nhap = st.number_input(
    "Nhập thu nhập trước thuế (triệu đồng/tháng)",
    min_value=0.0,
    value=20.0
)

nguoi_phu_thuoc = st.number_input(
    "Số người phụ thuộc",
    min_value=0,
    value=0
)

# Nút tính toán
if st.button("Tính thuế"):

    # Giảm trừ gia cảnh
    giam_tru_ban_than = 11
    giam_tru_phu_thuoc = 4.4 * nguoi_phu_thuoc

    # Thu nhập tính thuế
    tn_tinh_thue = thu_nhap - giam_tru_ban_than - giam_tru_phu_thuoc

    if tn_tinh_thue <= 0:
        st.success("Không phát sinh thuế TNCN.")
        st.write("Thuế phải nộp: **0 triệu đồng**")
    else:

        # Tính thuế lũy tiến từng phần
        thue = 0

        bac_thue = [
            (5, 0.05),
            (5, 0.10),
            (8, 0.15),
            (14, 0.20),
            (20, 0.25),
            (28, 0.30),
            (float('inf'), 0.35)
        ]

        thu_nhap_con_lai = tn_tinh_thue

        for muc, ty_le in bac_thue:
            if thu_nhap_con_lai > 0:
                phan_tinh_thue = min(thu_nhap_con_lai, muc)
                thue += phan_tinh_thue * ty_le
                thu_nhap_con_lai -= phan_tinh_thue

        thu_nhap_sau_thue = thu_nhap - thue

        st.success("Kết quả tính toán")

        st.write(
            f"📌 Thu nhập tính thuế: **{tn_tinh_thue:,.2f} triệu đồng**"
        )

        st.write(
            f"📌 Thuế TNCN phải nộp: **{thue:,.2f} triệu đồng**"
        )

        st.write(
            f"📌 Thu nhập sau thuế: **{thu_nhap_sau_thue:,.2f} triệu đồng**"
        )
