# Copyright 2017-2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)


{
    "name": "Attachments on Swift storage",
    "summary": "Store assets and attachments on a Swift compatible object store",
    "version": "15.0.1.0.0",
    "author": "Camptocamp,Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "category": "Knowledge Management",
    "depends": ["base_attachment_object_storage"],
    # Real PyPI distribution names below, not the bare import names --
    # pip has no package literally named swiftclient (404) or a usably
    # installable keystoneclient (exists but with no installable
    # releases), verified live against pypi.org. This comment is
    # deliberately OUTSIDE the "python" list below: OdooForge's own
    # manifest scraper (services/worker/executors/build.go's
    # externalPythonDeps) isn't a real Python parser, just a regex that
    # captures every quoted substring between the list's own brackets --
    # a comment placed *inside* those brackets gets its own quoted words
    # and apostrophes scraped right along with the real dependencies,
    # confirmed live producing garbled bogus entries in the generated
    # Dockerfile.
    "external_dependencies": {
        "python": [
            "python-swiftclient",
            "python-keystoneclient",
            "keystoneauth1",
        ],
    },
    "website": "https://github.com/camptocamp/odoo-cloud-platform",
    "data": [],
    "installable": True,
}
