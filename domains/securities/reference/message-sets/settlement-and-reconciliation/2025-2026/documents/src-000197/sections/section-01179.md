---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.83 FormOfSecurity6Choice"]
file_pages: [1630]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.83 FormOfSecurity6Choice

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1630 to 1630.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1630

```text
Definition: Unique reference identifying the triparty collateral management transaction from the client's
point of view.
Datatype: "Max35Text" on page 2192
35.1.16.83  FormOfSecurity6Choice
Definition: Choice of format for the form of securities.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1630
Or}   Proprietary <Prtry> [1..1] ± 1630
35.1.16.83.1  Code <Cd>
Presence: [1..1]
Definition: Form of the security expressed as an ISO 20022 code.
Datatype: "FormOfSecurity1Code" on page 2079
CodeName Name Definition
BEAR Bearer The financial instrument does not specify
any registration of ownership, and is
payable to whomever possesses the
certificate.
REGD Registered Shareholder name of the financial
instrument appears in the corporation/
funds books.
35.1.16.83.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Form of the security expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.16.84  SecuritiesCertificate4
Definition: Physical representation of a security.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1630 March 2026
```

