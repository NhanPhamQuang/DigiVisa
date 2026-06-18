from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Visa Service UI")

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

POPULAR_COUNTRIES = [
    {"slug":"japan", "flag":"🇯🇵", "name":"Japan", "days":"5-7 days", "price":"$39", "region":"Asia", "visa_type":"Tourist Visa"},
    {"slug":"south-korea", "flag":"🇰🇷", "name":"South Korea", "days":"5-8 days", "price":"$45", "region":"Asia", "visa_type":"Tourist Visa"},
    {"slug":"australia", "flag":"🇦🇺", "name":"Australia", "days":"10-15 days", "price":"$59", "region":"Oceania", "visa_type":"Visitor Visa"},
    {"slug":"canada", "flag":"🇨🇦", "name":"Canada", "days":"14-21 days", "price":"$69", "region":"America", "visa_type":"Visitor Visa"},
    {"slug":"united-states", "flag":"🇺🇸", "name":"United States", "days":"15-30 days", "price":"$79", "region":"America", "visa_type":"B1/B2 Visa"},
    {"slug":"united-kingdom", "flag":"🇬🇧", "name":"United Kingdom", "days":"10-20 days", "price":"$65", "region":"Europe", "visa_type":"Standard Visitor Visa"},
    {"slug":"china", "flag":"🇨🇳", "name":"China", "days":"4-7 days", "price":"$35", "region":"Asia", "visa_type":"Tourist Visa"},
    {"slug":"taiwan", "flag":"🇹🇼", "name":"Taiwan", "days":"3-5 days", "price":"$29", "region":"Asia", "visa_type":"Travel Authorization"},
    {"slug":"singapore", "flag":"🇸🇬", "name":"Singapore", "days":"2-4 days", "price":"$25", "region":"Asia", "visa_type":"Entry Visa"},
    {"slug":"thailand", "flag":"🇹🇭", "name":"Thailand", "days":"2-5 days", "price":"$25", "region":"Asia", "visa_type":"Tourist Visa"},
    {"slug":"malaysia", "flag":"🇲🇾", "name":"Malaysia", "days":"2-4 days", "price":"$25", "region":"Asia", "visa_type":"eVisa"},
    {"slug":"vietnam", "flag":"🇻🇳", "name":"Vietnam", "days":"3-5 days", "price":"$29", "region":"Asia", "visa_type":"eVisa"},
    {"slug":"france", "flag":"🇫🇷", "name":"France", "days":"10-15 days", "price":"$59", "region":"Europe", "visa_type":"Schengen Visa"},
    {"slug":"germany", "flag":"🇩🇪", "name":"Germany", "days":"10-15 days", "price":"$59", "region":"Europe", "visa_type":"Schengen Visa"},
    {"slug":"italy", "flag":"🇮🇹", "name":"Italy", "days":"10-15 days", "price":"$55", "region":"Europe", "visa_type":"Schengen Visa"},
    {"slug":"spain", "flag":"🇪🇸", "name":"Spain", "days":"10-15 days", "price":"$55", "region":"Europe", "visa_type":"Schengen Visa"},
    {"slug":"india", "flag":"🇮🇳", "name":"India", "days":"3-5 days", "price":"$30", "region":"Asia", "visa_type":"eVisa"},
    {"slug":"united-arab-emirates", "flag":"🇦🇪", "name":"United Arab Emirates", "days":"3-6 days", "price":"$49", "region":"Middle East", "visa_type":"Tourist Visa"},
    {"slug":"turkey", "flag":"🇹🇷", "name":"Turkey", "days":"2-4 days", "price":"$35", "region":"Europe", "visa_type":"eVisa"},
    {"slug":"new-zealand", "flag":"🇳🇿", "name":"New Zealand", "days":"10-15 days", "price":"$59", "region":"Oceania", "visa_type":"Visitor Visa"},
]

ALL_COUNTRIES = POPULAR_COUNTRIES + [
    {"slug":"belgium", "flag":"🇧🇪", "name":"Belgium", "days":"10-15 days", "price":"$55", "region":"Europe", "visa_type":"Schengen Visa"},
    {"slug":"netherlands", "flag":"🇳🇱", "name":"Netherlands", "days":"10-15 days", "price":"$55", "region":"Europe", "visa_type":"Schengen Visa"},
    {"slug":"switzerland", "flag":"🇨🇭", "name":"Switzerland", "days":"10-15 days", "price":"$65", "region":"Europe", "visa_type":"Schengen Visa"},
    {"slug":"sweden", "flag":"🇸🇪", "name":"Sweden", "days":"10-15 days", "price":"$59", "region":"Europe", "visa_type":"Schengen Visa"},
    {"slug":"norway", "flag":"🇳🇴", "name":"Norway", "days":"10-15 days", "price":"$59", "region":"Europe", "visa_type":"Schengen Visa"},
    {"slug":"denmark", "flag":"🇩🇰", "name":"Denmark", "days":"10-15 days", "price":"$59", "region":"Europe", "visa_type":"Schengen Visa"},
    {"slug":"brazil", "flag":"🇧🇷", "name":"Brazil", "days":"7-12 days", "price":"$45", "region":"America", "visa_type":"Visitor Visa"},
    {"slug":"mexico", "flag":"🇲🇽", "name":"Mexico", "days":"5-10 days", "price":"$39", "region":"America", "visa_type":"Tourist Visa"},
]

VISA_DETAILS = {
    c["slug"]: {
        **c,
        "description": f"Guided {c['name']} visa application support with document checklist, fee overview, and application tracking.",
        "requirements": [
            "Passport valid for at least 6 months",
            "Recent passport-size photo",
            "Completed visa application form",
            "Flight booking or travel itinerary",
            "Hotel booking or invitation letter",
            "Proof of financial capacity",
            "Employment or student confirmation if applicable",
        ],
        "fees": [
            {"label": "Service fee", "amount": c["price"]},
            {"label": "Government / Embassy fee", "amount": "Depends on nationality"},
            {"label": "Urgent processing", "amount": "Optional add-on"},
        ],
        "steps": ["Check requirements", "Prepare documents", "Submit application", "Track processing", "Receive visa result"],
    }
    for c in ALL_COUNTRIES
}

PICKUPS = [
    {"city":"Ho Chi Minh City", "airport":"Tan Son Nhat Airport", "price":"$12", "tag":"Popular"},
    {"city":"Hanoi", "airport":"Noi Bai Airport", "price":"$15", "tag":"24/7"},
    {"city":"Da Nang", "airport":"Da Nang Airport", "price":"$14", "tag":"Best value"},
]


VISA_SERVICE_PAGES = {
    "tourist-visa": ("Tourist Visa", "Apply for short-term travel visas with guided document preparation and application tracking."),
    "business-visa": ("Business Visa", "Support for business trips, meetings, conferences, and commercial travel documents."),
    "student-visa": ("Student Visa", "Study abroad visa support from requirement checking to document submission."),
    "visa-extension": ("Visa Extension", "Guidance for extending your stay while keeping your documents organized."),
    "urgent-processing": ("Urgent Processing", "Priority support for time-sensitive visa applications and last-minute travel plans."),
}

RESOURCE_PAGES = {
    "visa-guides": ("Visa Guides", "Step-by-step articles that explain application requirements, timelines, and common mistakes."),
    "travel-tips": ("Travel Tips", "Practical airport, document, packing, and arrival tips for smoother trips."),
    "faq": ("FAQ", "Frequently asked questions about visa applications, documents, payment, and tracking."),
    "blog": ("Blog", "SEO-friendly travel and visa updates for popular destinations."),
}

FAST_TRACKS = [
    {"country":"Vietnam", "title":"Vietnam Fast Track", "price":"$25", "features":["Meet & assist", "Priority lane", "Arrival support"]},
    {"country":"Thailand", "title":"Thailand Fast Track", "price":"$35", "features":["Immigration support", "Priority lane", "Airport escort"]},
    {"country":"Indonesia", "title":"Bali Fast Track", "price":"$32", "features":["Arrival assistance", "Queue support", "Private escort"]},
]

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {
        "request": request,
        "countries": POPULAR_COUNTRIES[:20],
        "pickups": PICKUPS,
        "fast_tracks": FAST_TRACKS,
        "active": "home"
    })

@app.get("/countries")
def countries(request: Request):
    return templates.TemplateResponse("countries.html", {
        "request": request,
        "countries": ALL_COUNTRIES,
        "active": "visa"
    })

@app.get("/visa/{slug}")
def visa_destination_detail(slug: str, request: Request):
    destination = VISA_DETAILS.get(slug)
    if not destination:
        return templates.TemplateResponse("simple.html", {
            "request": request,
            "active": "visa",
            "title": "Destination not found",
            "subtitle": "Please go back to the country list and choose another destination.",
        })
    return templates.TemplateResponse("visa_detail.html", {
        "request": request,
        "active": "visa",
        "title": f"{destination['name']} Visa Details - VisaHub",
        "destination": destination,
    })

@app.get("/application")
def application_page(request: Request, destination: str = ""):
    selected = VISA_DETAILS.get(destination) or POPULAR_COUNTRIES[0]
    if isinstance(selected, dict) and "requirements" not in selected:
        selected = VISA_DETAILS.get(selected["slug"], selected)
    return templates.TemplateResponse("application.html", {
        "request": request,
        "active": "visa",
        "title": f"Start Application - {selected['name']} Visa",
        "destination": selected,
    })

@app.post("/payment")
def payment_page(request: Request):
    return templates.TemplateResponse("simple.html", {
        "request": request,
        "active": "visa",
        "title": "Payment",
        "subtitle": "Payment UI placeholder. In the next step, this can connect to order creation, payment gateway, and application tracking.",
    })

@app.get("/visa-services")
def visa_services(request: Request):
    return templates.TemplateResponse("simple.html", {
        "request": request,
        "active": "visa",
        "title": "Visa Services",
        "subtitle": "Tourist visa, business visa, student visa, urgent processing, and requirement checking.",
    })

@app.get("/travel-resources")
def travel_resources(request: Request):
    return templates.TemplateResponse("simple.html", {
        "request": request,
        "active": "resources",
        "title": "Travel Resources",
        "subtitle": "Visa guides, country requirements, travel tips, FAQ, and useful travel updates.",
    })

@app.get("/visa-services/{slug}")
def visa_service_detail(slug: str, request: Request):
    title, subtitle = VISA_SERVICE_PAGES.get(slug, ("Visa Services", "Choose the right visa service for your trip."))
    return templates.TemplateResponse("simple.html", {
        "request": request,
        "active": "visa",
        "title": title,
        "subtitle": subtitle,
    })

@app.get("/travel-resources/{slug}")
def travel_resource_detail(slug: str, request: Request):
    title, subtitle = RESOURCE_PAGES.get(slug, ("Travel Resources", "Useful guides and travel information for international trips."))
    return templates.TemplateResponse("simple.html", {
        "request": request,
        "active": "resources",
        "title": title,
        "subtitle": subtitle,
    })

@app.get("/signup")
def signup_page(request: Request):
    return templates.TemplateResponse("auth.html", {
        "request": request,
        "active": "auth",
        "title": "Sign up - VisaHub",
        "mode": "signup",
        "action": "/signup",
        "eyebrow": "Create account",
        "heading": "Start your visa journey with confidence.",
        "description": "Create an account to save traveler information, upload documents, and track visa applications in one place.",
        "form_title": "Sign up",
        "form_subtitle": "Enter your details to create your VisaHub account.",
    })

@app.post("/signup")
def signup_submit(request: Request):
    return templates.TemplateResponse("simple.html", {
        "request": request,
        "active": "auth",
        "title": "Account Created",
        "subtitle": "Sign up form submitted successfully. Backend authentication can be connected later.",
    })

@app.get("/signin")
def signin_page(request: Request):
    return templates.TemplateResponse("auth.html", {
        "request": request,
        "active": "auth",
        "title": "Sign in - VisaHub",
        "mode": "signin",
        "action": "/signin",
        "eyebrow": "Welcome back",
        "heading": "Access your applications and travel services.",
        "description": "Sign in to continue your visa application, manage uploaded documents, and check processing status.",
        "form_title": "Sign in",
        "form_subtitle": "Use your email and password to access your account.",
    })

@app.post("/signin")
def signin_submit(request: Request):
    return templates.TemplateResponse("simple.html", {
        "request": request,
        "active": "auth",
        "title": "Signed In",
        "subtitle": "Sign in form submitted successfully. Backend authentication can be connected later.",
    })

@app.get("/profile")
def profile(request: Request):
    return templates.TemplateResponse("profile.html", {
        "request": request,
        "active": "profile",
        "title": "My Profile - VisaHub",
    })

@app.post("/profile")
def profile_submit(request: Request):
    return templates.TemplateResponse("simple.html", {
        "request": request,
        "active": "profile",
        "title": "Profile Saved",
        "subtitle": "Profile form submitted successfully. Backend profile storage and passport upload can be connected later.",
    })

ADMIN_ROWS = [
    {"id": "VH-1024", "initials": "VA", "customer": "Nguyen Van A", "email": "traveler1@example.com", "service": "Japan Tourist Visa", "status": "Pending", "status_class": "status-pending", "amount": "$39", "updated": "Today"},
    {"id": "VH-1025", "initials": "TT", "customer": "Tran Thu Trang", "email": "traveler2@example.com", "service": "Korea Tourist Visa", "status": "Processing", "status_class": "status-processing", "amount": "$49", "updated": "2h ago"},
    {"id": "VH-1026", "initials": "PL", "customer": "Pham Long", "email": "traveler3@example.com", "service": "Australia Visitor Visa", "status": "Completed", "status_class": "status-completed", "amount": "$59", "updated": "Yesterday"},
    {"id": "VH-1027", "initials": "MN", "customer": "Mai Nguyen", "email": "traveler4@example.com", "service": "Canada Visitor Visa", "status": "Need review", "status_class": "status-issue", "amount": "$69", "updated": "3d ago"},
    {"id": "VH-1028", "initials": "LM", "customer": "Le Minh", "email": "traveler5@example.com", "service": "USA Tourist Visa", "status": "Pending", "status_class": "status-pending", "amount": "$79", "updated": "Last week"},
    {"id": "VH-1029", "initials": "HA", "customer": "Hoang Anh", "email": "traveler6@example.com", "service": "UK Visitor Visa", "status": "Processing", "status_class": "status-processing", "amount": "$89", "updated": "Today"},
    {"id": "VH-1030", "initials": "DB", "customer": "Do Bao", "email": "traveler7@example.com", "service": "Singapore Tourist Visa", "status": "Completed", "status_class": "status-completed", "amount": "$39", "updated": "2h ago"},
    {"id": "VH-1031", "initials": "VL", "customer": "Vu Linh", "email": "traveler8@example.com", "service": "Thailand Tourist Visa", "status": "Need review", "status_class": "status-issue", "amount": "$49", "updated": "Yesterday"},
    {"id": "VH-1032", "initials": "DK", "customer": "Dang Khoa", "email": "traveler9@example.com", "service": "France Schengen Visa", "status": "Pending", "status_class": "status-pending", "amount": "$59", "updated": "3d ago"},
    {"id": "VH-1033", "initials": "BH", "customer": "Bui Han", "email": "traveler10@example.com", "service": "Germany Schengen Visa", "status": "Processing", "status_class": "status-processing", "amount": "$69", "updated": "Last week"},
    {"id": "VH-1034", "initials": "VN", "customer": "Vo Nhi", "email": "traveler11@example.com", "service": "Japan Tourist Visa", "status": "Completed", "status_class": "status-completed", "amount": "$79", "updated": "Today"},
    {"id": "VH-1035", "initials": "PQ", "customer": "Phan Quoc", "email": "traveler12@example.com", "service": "Korea Tourist Visa", "status": "Need review", "status_class": "status-issue", "amount": "$89", "updated": "2h ago"},
    {"id": "VH-1036", "initials": "LN", "customer": "Ly Nam", "email": "traveler13@example.com", "service": "Australia Visitor Visa", "status": "Pending", "status_class": "status-pending", "amount": "$39", "updated": "Yesterday"},
    {"id": "VH-1037", "initials": "TV", "customer": "Truong Vy", "email": "traveler14@example.com", "service": "Canada Visitor Visa", "status": "Processing", "status_class": "status-processing", "amount": "$49", "updated": "3d ago"},
    {"id": "VH-1038", "initials": "HT", "customer": "Huynh Tam", "email": "traveler15@example.com", "service": "USA Tourist Visa", "status": "Completed", "status_class": "status-completed", "amount": "$59", "updated": "Last week"},
    {"id": "VH-1039", "initials": "NS", "customer": "Ngo Son", "email": "traveler16@example.com", "service": "UK Visitor Visa", "status": "Need review", "status_class": "status-issue", "amount": "$69", "updated": "Today"},
    {"id": "VH-1040", "initials": "DM", "customer": "Dinh My", "email": "traveler17@example.com", "service": "Singapore Tourist Visa", "status": "Pending", "status_class": "status-pending", "amount": "$79", "updated": "2h ago"},
    {"id": "VH-1041", "initials": "CD", "customer": "Cao Dat", "email": "traveler18@example.com", "service": "Thailand Tourist Visa", "status": "Processing", "status_class": "status-processing", "amount": "$89", "updated": "Yesterday"},
    {"id": "VH-1042", "initials": "TQ", "customer": "Ta Quyen", "email": "traveler19@example.com", "service": "France Schengen Visa", "status": "Completed", "status_class": "status-completed", "amount": "$39", "updated": "3d ago"},
    {"id": "VH-1043", "initials": "LP", "customer": "La Phuong", "email": "traveler20@example.com", "service": "Germany Schengen Visa", "status": "Need review", "status_class": "status-issue", "amount": "$49", "updated": "Last week"},
    {"id": "VH-1044", "initials": "CH", "customer": "Chau Huy", "email": "traveler21@example.com", "service": "Japan Tourist Visa", "status": "Pending", "status_class": "status-pending", "amount": "$59", "updated": "Today"},
    {"id": "VH-1045", "initials": "LC", "customer": "Lam Chi", "email": "traveler22@example.com", "service": "Korea Tourist Visa", "status": "Processing", "status_class": "status-processing", "amount": "$69", "updated": "2h ago"},
    {"id": "VH-1046", "initials": "TB", "customer": "Thai Bao", "email": "traveler23@example.com", "service": "Australia Visitor Visa", "status": "Completed", "status_class": "status-completed", "amount": "$79", "updated": "Yesterday"},
    {"id": "VH-1047", "initials": "QY", "customer": "Quach Yen", "email": "traveler24@example.com", "service": "Canada Visitor Visa", "status": "Need review", "status_class": "status-issue", "amount": "$89", "updated": "3d ago"},
    {"id": "VH-1048", "initials": "KA", "customer": "Kieu An", "email": "traveler25@example.com", "service": "USA Tourist Visa", "status": "Pending", "status_class": "status-pending", "amount": "$39", "updated": "Last week"}
]


ADMIN_DESTINATIONS = [
    {"slug":"japan", "flag":"🇯🇵", "name":"Japan", "price":"$39", "status":"Active", "updated":"Today", "documents":["Passport", "Portrait photo", "Bank statement", "Travel itinerary", "Hotel booking"]},
    {"slug":"south-korea", "flag":"🇰🇷", "name":"South Korea", "price":"$45", "status":"Active", "updated":"2h ago", "documents":["Passport", "Portrait photo", "Bank statement", "Employment letter"]},
    {"slug":"australia", "flag":"🇦🇺", "name":"Australia", "price":"$59", "status":"Active", "updated":"Yesterday", "documents":["Passport", "Portrait photo", "Bank statement", "Employment letter", "Travel itinerary"]},
    {"slug":"canada", "flag":"🇨🇦", "name":"Canada", "price":"$69", "status":"Active", "updated":"3d ago", "documents":["Passport", "Portrait photo", "Bank statement", "Invitation letter"]},
    {"slug":"united-states", "flag":"🇺🇸", "name":"United States", "price":"$79", "status":"Active", "updated":"Last week", "documents":["Passport", "Portrait photo", "Employment letter", "Previous visa"]},
    {"slug":"france", "flag":"🇫🇷", "name":"France", "price":"$59", "status":"Archived", "updated":"Last month", "documents":["Passport", "Portrait photo", "Hotel booking", "Flight booking"]},
    {"slug":"germany", "flag":"🇩🇪", "name":"Germany", "price":"$59", "status":"Archived", "updated":"Last month", "documents":["Passport", "Portrait photo", "Travel itinerary", "Hotel booking"]},
]

ADMIN_DOCUMENT_OPTIONS = [
    "Passport", "Portrait photo", "Bank statement", "Employment letter", "Travel itinerary",
    "Hotel booking", "Flight booking", "Invitation letter", "Business license", "Previous visa"
]

def get_destination_or_default(slug: str):
    return next((item for item in ADMIN_DESTINATIONS if item["slug"] == slug), ADMIN_DESTINATIONS[0])

ADMIN_PAGE_CONFIG = {
    "dashboard": ("Dashboard", "All recent service activities", "Recent orders", "Monitor visa, airport pickup, and fast track operations in one place."),
    "visa_orders": ("Visa orders", "Visa application operations", "Visa application orders", "Review passport uploads, documents, payment, and processing status."),
    "destination": ("Destination", "Visa destination management", "Destination list", "Manage supported countries, visa types, fees, and document checklists."),
    "pickup_orders": ("Airport pickup orders", "Airport pickup operations", "Pickup bookings", "Track airport, customer arrival time, assigned driver, and service status."),
    "driver": ("Driver", "Driver management", "Driver list", "Manage driver availability, vehicle details, and assigned pickup orders."),
    "fast_track_orders": ("Fast track orders", "Fast track operations", "Fast track bookings", "Monitor meet-and-assist orders, airport partners, and priority lane service."),
    "partner": ("Partner", "Partner management", "Partner list", "Manage airport partners, fast track providers, and service coverage."),
    "statistics": ("Statistics", "Business analytics", "Performance summary", "Track revenue, order volume, conversion, and service completion rate."),
    "admin_profile": ("Admin profile", "Account settings", "Admin account", "Manage admin identity, password, notification, and access settings."),
}


def render_admin(request: Request, active_key: str = "dashboard"):
    page_title, eyebrow, table_title, table_subtitle = ADMIN_PAGE_CONFIG.get(active_key, ADMIN_PAGE_CONFIG["dashboard"])

    selected_status = request.query_params.get("status", "All")
    try:
        current_page = int(request.query_params.get("page", "1"))
    except ValueError:
        current_page = 1

    page_size = 10
    available_statuses = ["All", "Pending", "Processing", "Need review", "Completed"]
    filtered_rows = ADMIN_ROWS
    if active_key == "visa_orders" and selected_status != "All":
        filtered_rows = [row for row in ADMIN_ROWS if row["status"] == selected_status]

    total_orders = len(filtered_rows)
    total_pages = max(1, (total_orders + page_size - 1) // page_size)
    current_page = max(1, min(current_page, total_pages))
    start_index = (current_page - 1) * page_size
    paginated_rows = filtered_rows[start_index:start_index + page_size]

    status_counts = {status: len([row for row in ADMIN_ROWS if row["status"] == status]) for status in available_statuses if status != "All"}
    status_counts["All"] = len(ADMIN_ROWS)

    return templates.TemplateResponse("admin_dashboard.html", {
        "request": request,
        "title": f"{page_title} - VisaHub Admin",
        "page_title": page_title,
        "admin_active": active_key,
        "rows": paginated_rows,
        "all_rows_count": len(ADMIN_ROWS),
        "table_title": table_title,
        "table_subtitle": table_subtitle,
        "eyebrow": eyebrow,
        "available_statuses": available_statuses,
        "selected_status": selected_status,
        "status_counts": status_counts,
        "current_page": current_page,
        "total_pages": total_pages,
        "page_size": page_size,
        "total_orders": total_orders,
        "start_item": 0 if total_orders == 0 else start_index + 1,
        "end_item": min(start_index + page_size, total_orders),
    })

@app.get("/admin")
def admin_dashboard(request: Request):
    return render_admin(request, "dashboard")

@app.get("/admin/visa-orders")
def admin_visa_orders(request: Request):
    return render_admin(request, "visa_orders")

@app.get("/admin/destinations")
def admin_destinations(request: Request):
    status_filter = request.query_params.get("status", "active")
    if status_filter == "archived":
        destinations = [item for item in ADMIN_DESTINATIONS if item["status"] == "Archived"]
    else:
        status_filter = "active"
        destinations = [item for item in ADMIN_DESTINATIONS if item["status"] == "Active"]
    return templates.TemplateResponse("admin_destinations.html", {
        "request": request,
        "title": "Destinations - VisaHub Admin",
        "admin_active": "destination",
        "destinations": destinations,
        "status_filter": status_filter,
        "active_count": len([item for item in ADMIN_DESTINATIONS if item["status"] == "Active"]),
        "archived_count": len([item for item in ADMIN_DESTINATIONS if item["status"] == "Archived"]),
    })

@app.get("/admin/destinations/create")
def admin_create_destination(request: Request):
    return templates.TemplateResponse("admin_create_destination.html", {
        "request": request,
        "title": "Create Destination - VisaHub Admin",
        "admin_active": "destination",
    })

@app.post("/admin/destinations/create")
def admin_create_destination_submit(request: Request):
    return templates.TemplateResponse("simple.html", {
        "request": request,
        "active": "admin",
        "title": "Destination Created",
        "subtitle": "Create destination form submitted successfully. Backend storage can be connected later.",
    })

@app.get("/admin/destinations/{slug}/edit")
def admin_edit_destination(slug: str, request: Request):
    destination = get_destination_or_default(slug)
    return templates.TemplateResponse("admin_edit_destination.html", {
        "request": request,
        "title": f"Edit {destination['name']} - VisaHub Admin",
        "admin_active": "destination",
        "destination": destination,
        "document_options": ADMIN_DOCUMENT_OPTIONS,
    })

@app.post("/admin/destinations/{slug}/edit")
def admin_edit_destination_submit(slug: str, request: Request):
    return templates.TemplateResponse("simple.html", {
        "request": request,
        "active": "admin",
        "title": "Destination Updated",
        "subtitle": "Edit destination form submitted successfully. Backend update logic can be connected later.",
    })

@app.post("/admin/destinations/{slug}/archive")
def admin_archive_destination(slug: str, request: Request):
    return templates.TemplateResponse("simple.html", {
        "request": request,
        "active": "admin",
        "title": "Destination Archived",
        "subtitle": "Archive action submitted successfully. Backend archive logic can be connected later.",
    })

@app.post("/admin/destinations/{slug}/restore")
def admin_restore_destination(slug: str, request: Request):
    return templates.TemplateResponse("simple.html", {
        "request": request,
        "active": "admin",
        "title": "Destination Restored",
        "subtitle": "Restore action submitted successfully. Backend restore logic can be connected later.",
    })

@app.post("/admin/destinations/{slug}/delete")
def admin_delete_destination(slug: str, request: Request):
    return templates.TemplateResponse("simple.html", {
        "request": request,
        "active": "admin",
        "title": "Destination Deleted",
        "subtitle": "Delete action submitted successfully. Backend hard-delete logic can be connected later.",
    })

@app.get("/admin/airport-pickup-orders")
def admin_airport_pickup_orders(request: Request):
    return render_admin(request, "pickup_orders")

@app.get("/admin/drivers")
def admin_drivers(request: Request):
    return render_admin(request, "driver")

@app.get("/admin/fast-track-orders")
def admin_fast_track_orders(request: Request):
    return render_admin(request, "fast_track_orders")

@app.get("/admin/partners")
def admin_partners(request: Request):
    return render_admin(request, "partner")

@app.get("/admin/statistics")
def admin_statistics(request: Request):
    return render_admin(request, "statistics")

@app.get("/admin/profile")
def admin_profile(request: Request):
    return render_admin(request, "admin_profile")
