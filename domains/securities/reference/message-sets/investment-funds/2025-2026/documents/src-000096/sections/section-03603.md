---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.23 InvestorProfile2", "66.1.28.23.4 HighFrequencyTrading <HghFrqcyTradg>", "66.1.28.23.4.3 ConsolidationType <CnsldtnTp>", "66.1.28.23.4.3.1 Code <Cd>"]
file_pages: [4853]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.23.4.3.1 Code <Cd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4853 to 4853.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4853

```text
66.1.28.23.4.3.1  Code <Cd>
Presence: [1..1]
Definition: Consolidation type expressed as a code.
Datatype: "ConsolidationType1Code" on page 5288
CodeName Name Definition
GENL General Consolidation is general.
PART Participation Consolidation is at the level of the
participant.
66.1.28.23.4.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Consolidation type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.28.23.5  MarketMaker <MktMakr>
Presence: [0..1]
Definition: Information about the profile for a market marker.
MarketMaker <MktMakr> contains the following MarketMakerProfile2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ContractPeriod <CtrctPrd> [0..1] ± 4853
   Compliance <Cmplc> [0..1] Indicator 4854
   MaximumSpread <MaxSprd> [0..1] Rate 4854
   Discount <Dscnt> [0..1] Rate 4854
66.1.28.23.5.1  ContractPeriod <CtrctPrd>
Presence: [0..1]
Definition: Period of the contract.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4853 May 2026
```

