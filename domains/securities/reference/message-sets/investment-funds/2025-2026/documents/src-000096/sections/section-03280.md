---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.18 Financial Instrument", "66.1.18.13 SecurityIdentification19", "66.1.18.13.2 OtherIdentification <OthrId>", "66.1.18.13.2.2 Suffix <Sfx>"]
file_pages: [4517]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.18.13.2.2 Suffix <Sfx>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4517 to 4517.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4517

```text
Datatype: "Max35Text" on page 5403
66.1.18.13.2.2  Suffix <Sfx>
Presence: [0..1]
Definition: Identifies the suffix of the security identification.
Datatype: "Max16Text" on page 5402
66.1.18.13.2.3  Type <Tp>
Presence: [1..1]
Definition: Type of the identification.
Type <Tp> contains one of the following elements (see "IdentificationSource3Choice" on page 4550 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4550
Or}   Proprietary <Prtry> [1..1] Text 4550
66.1.18.13.3  Description <Desc>
Presence: [0..1]
Definition: Textual description of a security instrument.
Datatype: "Max140Text" on page 5402
66.1.18.14  FinancialInstrument13
Definition: Security that is a sub-set of an investment fund, and is governed by the same investment
fund policy, eg, dividend option or valuation currency.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 4517
   Name <Nm> [0..1] Text 4518
   SupplementaryIdentification <SplmtryId> [0..1] Text 4518
   ClassType <ClssTp> [0..1] Text 4518
   SecuritiesForm <SctiesForm> [0..1] CodeSet 4519
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 4519
Constraints
• FinancialInstrumentIdentificationGuideline
It is recommended that ISIN be used in Identification\SecurityIdentification3Choice.
66.1.18.14.1  Identification <Id>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4517 May 2026
```

