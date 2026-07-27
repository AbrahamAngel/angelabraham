from django.shortcuts import render
from django.http import Http404

def index(request):
    return render(request, "index.html")

PROJECTS = {
    "voiceassist": {
        "title": "VoiceAssist",
        "category": "AI / Speech Recognition",
        "tech_stack": "Python, OpenAI Whisper, FFmpeg, NLP",
        "image": "img/portfolio/voice.png",
        "github_url": "https://github.com/AbrahamAngel/voiceassist",
        "summary": "An AI-powered speech-to-text system built to improve medical communication accessibility for hearing-impaired patients during doctor consultations.",
        "highlights": [
            "Audio capture and preprocessing pipeline using MediaRecorder API and FFmpeg",
            "Integrated OpenAI Whisper to transcribe spoken medical instructions",
            "Lightweight NLP layer to simplify medical terminology and extract dosage/treatment info",
            "Rule-based risk detection to flag emergency-related keywords",
        ],
    },
    "event-registration": {
        "title": "Event Registration Management System",
        "category": "Web Application",
        "tech_stack": "Django, Django ORM, MySQL/PostgreSQL",
        "image": "img/portfolio/crob.png",
        "github_url": "https://github.com/AbrahamAngel/event-registration",
        "summary": "A web-based event registration platform enabling streamlined management of 7 technical events and supporting 50+ team registrations through a centralized system.",
        "highlights": [
            "Secure user authentication and team-based registration workflows",
            "Participants can browse events, access brochures, and complete structured registrations",
            "Relational database models designed and optimized using Django ORM",
            "Backend validation logic to prevent duplicate registrations and maintain data integrity",
            "Administrative dashboard for organizers to monitor registrations, control availability, and export participant data to Excel",
        ],
    },
    "blogging-platform": {
        "title": "Blogging Platform",
        "category": "Web Application",
        "tech_stack": "Django, Django ORM, SQLite",
        "image": "img/portfolio/blog.jpg",
        "live_url": "https://lnkd.in/eZMXGJ2r",
        "summary": "A full-stack blogging platform enabling users to create, edit, and publish blog posts through a dynamic web interface.",
        "highlights": [
            "Relational database models structured using Django ORM and SQLite for posts, comments, and users",
            "Interactive comment and threaded reply system for discussions within blog posts",
            "Search and browsing functionality based on blog titles for quick content discovery",
        ],
    },
}

def portfolio_details(request, slug):
    project = PROJECTS.get(slug)
    if project is None:
        raise Http404("Project not found")
    return render(request, "portfolio/portfolio_details.html", {"project": project})