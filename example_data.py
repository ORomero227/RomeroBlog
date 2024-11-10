import os
from database import User, BlogPost
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash
from datetime import date

load_dotenv()

def db_load_example_data(db):
    existing_admin = db.session.execute(
        db.select(User).where(User.email == os.getenv("ADMIN_EMAIL"))
    ).scalar()

    if not existing_admin:
        password_to_hash = os.getenv("ADMIN_PASSWORD")
        hashed_password = generate_password_hash(password_to_hash, method="pbkdf2:sha256")
        admin = User(
            name = os.getenv("ADMIN_NAME"),
            email = os.getenv("ADMIN_EMAIL"),
            password= hashed_password
        )
        db.session.add(admin)
        db.session.commit()
        existing_admin = admin

    if existing_admin is None:
        print("Error: existing_admin not found or was not created correctly.")
        return

    existing_posts = db.session.execute(db.select(BlogPost)).scalar()

    if not existing_posts:
        example_posts = [
            BlogPost(
                title="Building a Workout Tracker App Using React and Node.js",
                subtitle="A Step-by-Step Guide to Building a Full-Stack Project for Your Portfolio",
                date= date.today().strftime("%B %d, %Y"),
                body = "<p>Developing a workout tracker app is a fantastic way to showcase your skills in a full-stack environment. This tutorial takes you through each step of building a workout tracker from scratch using React for the frontend and Node.js for the backend. You&rsquo;ll learn how to structure components, manage data flow, and integrate authentication to keep user data secure. Follow along to build a functional, polished app for your portfolio that showcases your technical proficiency.</p>",
                img_url="https://img.freepik.com/free-photo/young-athletic-woman-having-cross-training-stationary-bike-gym_637285-2524.jpg?t=st=1731201471~exp=1731205071~hmac=9b810496acc337b916e6d3fc5cd6eef8090c11586f4ff2538f9380c65940cf75&w=996",
                card_img_url="https://img.freepik.com/free-photo/technology-app-development-wireless-e-commerce_53876-124044.jpg?t=st=1731202910~exp=1731206510~hmac=e7eda778a68cec2e62fb00ec581e7d776dc2eac3ec73754bbf5c04f297203484&w=996",
                author= existing_admin,
            ),
            BlogPost(
                title="Essential Cybersecurity Practices for Beginners",
                subtitle="A Guide to Safeguarding Your Applications and Personal Data",
                date=date.today().strftime("%B %d, %Y"),
                body="<p>Cybersecurity is no longer just a concern for big corporations; it&#39;s essential for everyone. In this post, we&rsquo;ll explore key cybersecurity practices that are easy for beginners to implement. From setting up two-factor authentication to regularly updating passwords and encrypting data, these steps will help protect your applications and personal data. We&rsquo;ll also touch on secure coding practices, making this guide especially useful for budding developers looking to add cybersecurity knowledge to their toolkit.</p>",
                img_url="https://img.freepik.com/free-photo/cybercriminal-using-ai-machine-learning-develop-zero-day-exploit_482257-88601.jpg?t=st=1731201557~exp=1731205157~hmac=59c3e97fc47422c8ee305dd3e9e112c9fe6089a33e2932e7c68a8a399829dd74&w=1060",
                card_img_url="https://img.freepik.com/free-photo/programming-background-with-person-working-with-codes-computer_23-2150010138.jpg?t=st=1731202826~exp=1731206426~hmac=951dfdff0f7e6659e6049a6aea7f87dbb96134acf9ed23fadf4eccfec2a6f5a0&w=996",
                author=existing_admin,
            ),
            BlogPost(
                title="Building Your First Django CRM: A Beginner's Guide",
                subtitle="Learn How to Develop a Simple CRM Application Using Django and PostgreSQL",
                date=date.today().strftime("%B %d, %Y"),
                body="<p>Creating a simple CRM with Django and PostgreSQL is a great way to learn how to handle data effectively in a real-world application. In this guide, you&rsquo;ll learn to set up a basic CRM from scratch, covering models, views, and templates while implementing database queries in PostgreSQL. This guide will also demonstrate Django&rsquo;s robust ORM and show you how to build a scalable, functional CRM application that can manage customer data, track sales, and improve business operations.</p>",
                img_url="https://img.freepik.com/free-photo/customer-relationship-management-concept_23-2150038409.jpg?t=st=1731202727~exp=1731206327~hmac=899d77a976e2bec04c63c1ce6f1f9797307d6370016f4a3cecb81f7075d89de9&w=996",
                card_img_url="https://img.freepik.com/free-photo/customer-relationship-management-concept_23-2150038398.jpg?t=st=1731202774~exp=1731206374~hmac=76fddbdede9c1951c9cd3e1aaf5659398d0f39143fc5628dfd2db7fd4caf11cf&w=996",
                author=existing_admin,
            ),
        ]

        for post in example_posts:
            db.session.add(post)
        db.session.commit()