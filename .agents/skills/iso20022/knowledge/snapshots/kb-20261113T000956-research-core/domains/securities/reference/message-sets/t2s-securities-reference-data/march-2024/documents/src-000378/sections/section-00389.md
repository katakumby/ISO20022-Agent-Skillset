---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.10 Miscellaneous", "13.1.10.2 OptionType8Choice", "13.1.10.2.2 Proprietary <Prtry>"]
file_pages: [482]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.10.2.2 Proprietary <Prtry>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 482 to 482.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 482

```text
CodeName Name Definition
PUTO Put Right to sell a quantity of an asset for an
agreed price at exercise date.
13.1.10.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Option type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 478 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 479
   Issuer <Issr> [1..1] Text 479
   SchemeName <SchmeNm> [0..1] Text 479
13.1.10.3  FormOfSecurity8Choice
Definition: Choice of format for form of security.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 482
Or}   Proprietary <Prtry> [1..1] ± 482
13.1.10.3.1  Code <Cd>
Presence: [1..1]
Definition: Form of security expressed as an ISO 20022 code.
Datatype: "FormOfSecurity1Code" on page 514
CodeName Name Definition
BEAR Bearer The financial instrument does not specify
any registration of ownership, and is
payable to whomever possesses the
certificate.
REGD Registered Shareholder name of the financial
instrument appears in the corporation/
funds books.
13.1.10.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Form of security expressed as a proprietary code.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 482 March 2024
```

