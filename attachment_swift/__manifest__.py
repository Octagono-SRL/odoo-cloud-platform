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
    "external_dependencies": {
        "python": [
            # Real PyPI distribution names, not the bare import names: pip
            # has no package literally called "swiftclient" (404) or a
            # usably-installable "keystoneclient" (exists but with no
            # installable releases) — verified live against pypi.org.
            # This mismatch isn't cosmetic: a build/upgrade's combined pip
            # install for every discovered module's declared deps hard-
            # fails on the first bad name and falls back to installing
            # every dependency one at a time, which drops any other
            # module's exact-pinned dependency (e.g. l10n_do_dgii_factura_
            # electronica's own cryptography/pyOpenSSL pins) to whatever a
            # later, unrelated, unpinned package happens to pull in
            # transitively instead.
            "python-swiftclient",
            "python-keystoneclient",
            "keystoneauth1",
        ],
    },
    "website": "https://github.com/camptocamp/odoo-cloud-platform",
    "data": [],
    "installable": True,
}
