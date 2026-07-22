TỔNG HỢP FILE LIÊN QUAN ĐẾN SERVER - GAME TIÊN NGHỊCH MOBILE (com.joyplay.tiennghich)
========================================================================

1. CommonSdkGame.ini
   - API gateway chính của SDK: apiUrl = https://gpartner.tiennghichmobile.com
   - Chứa gid, pid, mid, sdkversion dùng để xác thực SDK

2. CommonSdkMsdk.ini
   - Cấu hình phụ của SDK (showExit)

3. index.html / index_vn.html
   - File khởi chạy game (Egret engine)
   - index_vn.html có hardcode: GameConfig.resPath = "https://sever-247.onrender.com/resource"
     (server chứa resource/asset cho bản Việt Nam)

4. game_manifest.json
   - Danh sách các file JS được load khi khởi động game (không chứa URL server)

5. privacypolicy_url.txt / userargeement_url.txt
   - Link chính sách bảo mật & điều khoản sử dụng (h5.xiwangame.com) - không phải server game

6. socket.min_17e20039.js
   - Module xử lý kết nối Socket/WebSocket của engine Egret
   - Không hardcode địa chỉ server - địa chỉ được truyền động lúc runtime

7. main.min_8f5780e8.js
   - File logic chính của game (9MB, đã minify)
   - Chứa các API/CDN được hardcode, xem chi tiết trong "danh_sach_url_trich_xuat.txt"

8. danh_sach_url_trich_xuat.txt
   - Toàn bộ URL http/https trích xuất được từ main.min_8f5780e8.js, bao gồm:
     * API: xnh5api.tiennghichmobile.com, xnh5api.51haodong.com, xnh5api2/5.btshidai.com
     * CDN resource: xnh5cdn.51haodong.com, xnh5cdn.btshidai.com, xnh5cdn3.btshidai.com
     * Release/update: xnh5release.mcjdhjj.com
     * IP hardcode: 42.194.133.123
     * Khác: iodek.qwhytech.com (có thể tracking), discord, facebook, app store links...

9. xapk_manifest.json
   - Manifest gốc của gói XAPK (package name, version, permissions, split APKs)
