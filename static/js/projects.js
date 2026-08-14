document.addEventListener("DOMContentLoaded", function () {

    const filters = document.querySelectorAll(".project-filter");
    const projects = document.querySelectorAll(".project-item");

    filters.forEach(function (filter) {

        filter.addEventListener("click", function () {

            filters.forEach(function (item) {
                item.classList.remove("active");
            });

            this.classList.add("active");

            const selectedCategory = this.dataset.filter;

            projects.forEach(function (project) {

                const projectCategory =
                    project.dataset.category;

                if (
                    selectedCategory === "all" ||
                    selectedCategory === projectCategory
                ) {

                    project.classList.remove("hidden");

                    project.classList.remove(
                        "filter-animation"
                    );

                    void project.offsetWidth;

                    project.classList.add(
                        "filter-animation"
                    );

                } else {

                    project.classList.add("hidden");

                }

            });

        });

    });

});

document.addEventListener("DOMContentLoaded", function () {

    const image = document.querySelector(
        ".project-main-image img"
    );

    if (image) {

        image.addEventListener("load", function () {

            image.classList.add("loaded");

        });

    }

});


document.addEventListener("DOMContentLoaded", function () {

    /* =====================================================
       Animation des éléments
    ====================================================== */

    const animatedElements = document.querySelectorAll(
        ".contact-panel, " +
        ".reason-card, " +
        ".social-card, " +
        ".availability-section"
    );

    const observer = new IntersectionObserver(
        function (entries) {

            entries.forEach(function (entry) {

                if (entry.isIntersecting) {

                    entry.target.classList.add(
                        "contact-visible"
                    );

                }

            });

        },
        {
            threshold: 0.12
        }
    );


    animatedElements.forEach(function (element) {
        observer.observe(element);
    });


    /* =====================================================
       Bouton d'envoi
    ====================================================== */

    const form = document.querySelector(".contact-form");
    const submitButton = document.querySelector(".contact-submit");

    if (form && submitButton) {

        form.addEventListener("submit", function () {

            submitButton.classList.add("sending");

            submitButton.querySelector("span").textContent =
                "Envoi en cours...";

        });

    }


    /* =====================================================
       Effet focus formulaire
    ====================================================== */

    const inputs = document.querySelectorAll(
        ".contact-input"
    );

    inputs.forEach(function (input) {

        input.addEventListener("focus", function () {

            this.closest(
                ".form-group"
            ).classList.add("input-active");

        });

        input.addEventListener("blur", function () {

            this.closest(
                ".form-group"
            ).classList.remove("input-active");

        });

    });

});