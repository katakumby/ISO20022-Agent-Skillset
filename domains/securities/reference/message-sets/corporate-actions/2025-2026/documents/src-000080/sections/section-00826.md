---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.17 Party Identification", "16.1.17.6 Party38Choice"]
file_pages: [1044]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.17.6 Party38Choice

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1044 to 1044.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1044

```text
16.1.17.6  Party38Choice
Definition: Nature or use of the account.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrganisationIdentification <OrgId> [1..1] ± 1044
Or}   PrivateIdentification <PrvtId> [1..1] ± 1044
16.1.17.6.1  OrganisationIdentification <OrgId>
Presence: [1..1]
Definition: Unique and unambiguous way to identify an organisation.
OrganisationIdentification <OrgId> contains the following elements (see
"OrganisationIdentification29" on page 1032 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AnyBIC <AnyBIC> [0..1] IdentifierSet C1 1032
   LEI <LEI> [0..1] IdentifierSet 1032
   Other <Othr> [0..*]  1032
     Identification <Id> [1..1] Text 1033
     SchemeName <SchmeNm> [0..1]  1033
{Or       Code <Cd> [1..1] CodeSet 1033
Or}       Proprietary <Prtry> [1..1] Text 1033
     Issuer <Issr> [0..1] Text 1033
16.1.17.6.2  PrivateIdentification <PrvtId>
Presence: [1..1]
Definition: Unique and unambiguous identification of a person, for example a passport.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1044 February 2026
```

