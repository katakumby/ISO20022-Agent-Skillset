---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.59 BeneficiaryCertificationType10Choice"]
file_pages: [982]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.59 BeneficiaryCertificationType10Choice

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 982 to 982.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 982

```text
Definition: Indicates whether the report is complete or contains changes only.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.15.59  BeneficiaryCertificationType10Choice
Definition: Choice between a standard code or proprietary code to specify the type of beneficiary
certification required.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 982
Or}   Proprietary <Prtry> [1..1] ± 982
16.1.15.59.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the type of certification required.
Datatype: "BeneficiaryCertificationType5Code" on page 1164
CodeName Name Definition
ACCI AccreditedInvestor The holder of the security has to
irrevocably certify that it is an Accredited
Investor as defined in US Securities and
Exchange Commission Regulation D.
NCOM NonCompany The holder of the security has to certify
he is an Non-Company related person.
QIBB QIBCertification The holder of the security has to
irrevocably certify that it is a Qualified
Institutional Buyer as defined in US
Securities and Exchange Commission
Rule 144A.
16.1.15.59.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the type of certification required.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 982 February 2026
```

