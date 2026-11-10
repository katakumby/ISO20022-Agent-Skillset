---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.42 PartyRole2Choice", "66.1.30.42.2 Proprietary <Prtry>"]
file_pages: [5040]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.42.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5040 to 5040.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5040

```text
CodeName Name Definition
resulting in unit or cash account
movements to the investor or the
investor's intermediary. It responds to
inquiries concerning account status, and
processes the income distribution.
TRAN TransmittingAgent Party that transmits the instruction,
advice, notification or report.
66.1.30.42.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Role expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.30.43  Intermediary43
Definition: Party that provides services to investors relating to financial products.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 5040
   Account <Acct> [0..1]  5041
     Identification <Id> [0..1] Text 5041
     AccountServicer <AcctSvcr> [1..1] ± 5041
   Role <Role> [0..1] ± 5041
   ContactPerson <CtctPrsn> [0..1] ± 5041
66.1.30.43.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identifier of the intermediary.
Identification <Id> contains the following elements (see "PartyIdentification139" on page 5043 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5040 May 2026
```

