---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.23 InvestorProfile2", "66.1.28.23.3 Treasury <Trsr>", "66.1.28.23.3.2 TraderType <TradrTp>", "66.1.28.23.3.2.2 Proprietary <Prtry>"]
file_pages: [4851]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.23.3.2.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4851 to 4851.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4851

```text
CodeName Name Definition
CUST Custodian Party that safekeeps and administers
assets on behalf of the owner.
INVS Investor Party, either an individual or
organisation, whose assets are being
invested.
66.1.28.23.3.2.2  Proprietary <Prtry>
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
66.1.28.23.3.3  Rate <Rate>
Presence: [1..1]
Definition: Tax rate.
Datatype: "PercentageRate" on page 5401
66.1.28.23.4  HighFrequencyTrading <HghFrqcyTradg>
Presence: [0..1]
Definition: Information about the profile for high frequency trading.
HighFrequencyTrading <HghFrqcyTradg> contains the following HighFrequencyTradingProfile1
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Date <Dt> [0..1] Date 4851
   SettlementFrequency <SttlmFrqcy> [0..1]  4852
{Or     Code <Cd> [1..1] CodeSet 4852
Or}     Proprietary <Prtry> [1..1] ± 4852
   ConsolidationType <CnsldtnTp> [0..1]  4852
{Or     Code <Cd> [1..1] CodeSet 4853
Or}     Proprietary <Prtry> [1..1] ± 4853
66.1.28.23.4.1  Date <Dt>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4851 May 2026
```

