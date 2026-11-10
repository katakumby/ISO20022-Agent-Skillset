---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.15 InvestorCapacity4Choice"]
file_pages: [1547]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.15 InvestorCapacity4Choice

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1547 to 1547.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1547

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.16.15  InvestorCapacity4Choice
Definition: Choice of format for the investor capacity.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1547
Or}   Proprietary <Prtry> [1..1] ± 1547
35.1.16.15.1  Code <Cd>
Presence: [1..1]
Definition: Investor capacity expressed as an ISO 20022 code.
Datatype: "Eligibility1Code" on page 2061
CodeName Name Definition
ELIG EligibleCounterparty Eligible customers are the most
sophisticated level of investor, able to
opt out of some the protections afforded
by conduct of business rules.
RETL RetailClient Retail customers are the least
sophisticated level of investor.
PROF ProfessionalClient Professional customers are, for example,
investment firms, credit institutions,
insurance companies.
35.1.16.15.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Investor capacity expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1547 March 2026
```

