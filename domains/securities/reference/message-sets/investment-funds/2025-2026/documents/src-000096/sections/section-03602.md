---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.23 InvestorProfile2", "66.1.28.23.4 HighFrequencyTrading <HghFrqcyTradg>", "66.1.28.23.4.2 SettlementFrequency <SttlmFrqcy>"]
file_pages: [4852]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.23.4.2 SettlementFrequency <SttlmFrqcy>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4852 to 4852.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4852

```text
Definition: Date on which the investor starts high frequency trading.
Datatype: "ISODate" on page 5388
66.1.28.23.4.2  SettlementFrequency <SttlmFrqcy>
Presence: [0..1]
Definition: Frequency of settlement.
SettlementFrequency <SttlmFrqcy> contains one of the following SettlementFrequency1Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4852
Or}   Proprietary <Prtry> [1..1] ± 4852
66.1.28.23.4.2.1  Code <Cd>
Presence: [1..1]
Definition: Settlement frequency expressed as a code.
Datatype: "EventFrequency10Code" on page 5297
CodeName Name Definition
DAIL Daily Event takes place every day.
ADHO Adhoc Event takes place as necessary.
66.1.28.23.4.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Settlement frequency expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.28.23.4.3  ConsolidationType <CnsldtnTp>
Presence: [0..1]
Definition: Specifies whether consolidation is done generally or at the level of segregated account.
ConsolidationType <CnsldtnTp> contains one of the following ConsolidationType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4853
Or}   Proprietary <Prtry> [1..1] ± 4853
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4852 May 2026
```

