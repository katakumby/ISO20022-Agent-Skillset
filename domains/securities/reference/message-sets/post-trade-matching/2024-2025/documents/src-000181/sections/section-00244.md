---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.11 CentralCounterPartyEligibility4Choice", "7.1.19.11.2 Proprietary <Prtry>"]
file_pages: [302]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.11.2 Proprietary <Prtry>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 302 to 302.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 302

```text
Definition: Specifies whether the settlement transaction is CCP (Central Counterparty) eligible.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
7.1.19.11.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Central counterparty eligibility information expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.19.12  InvestorCapacity4Choice
Definition: Choice of format for the investor capacity.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 302
Or}   Proprietary <Prtry> [1..1] ± 302
7.1.19.12.1  Code <Cd>
Presence: [1..1]
Definition: Investor capacity expressed as an ISO 20022 code.
Datatype: "Eligibility1Code" on page 624
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
7.1.19.12.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Investor capacity expressed as a proprietary code.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 302 February 2025
```

