---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.14 Identification Information", "6.1.14.4 GenericIdentification32", "6.1.14.4.4 ShortName <ShrtNm>"]
file_pages: [841]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.14.4.4 ShortName <ShrtNm>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 841 to 841.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 841

```text
CodeName Name Definition
ITAG IntermediaryAgent Party acting on behalf of other parties to
process or forward data to other parties.
ACQR Acquirer Entity acquiring card transactions.
CISS CardIssuer Party that issues cards.
TAXH TaxAuthority Tax authority.
6.1.14.4.4  ShortName <ShrtNm>
Presence: [0..1]
Definition: Name of the entity.
Datatype: "Max35Text" on page 916
6.1.14.5  GenericIdentification1
Definition: Information related to an identification, for example party identification or account
identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 841
   SchemeName <SchmeNm> [0..1] Text 841
   Issuer <Issr> [0..1] Text 841
6.1.14.5.1  Identification <Id>
Presence: [1..1]
Definition: Identification assigned by an institution.
Datatype: "Max35Text" on page 916
6.1.14.5.2  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
Datatype: "Max35Text" on page 916
6.1.14.5.3  Issuer <Issr>
Presence: [0..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 916
6.1.14.6  GenericIdentification30
Definition: Information related to an identification, for example, party identification or account
identification.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
841 March 2026
```

