---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.14 InvestmentAccount75", "66.1.24.14.15 AccumulationRightReference <AcmltnRghtRef>"]
file_pages: [4653]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.14.15 AccumulationRightReference <AcmltnRghtRef>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4653 to 4653.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4653

```text
LetterIntentDetails <LttrInttDtls> contains the following elements (see "LetterIntent1" on page 4824
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LetterIntentReference <LttrInttRef> [1..1] Text 4825
   Amount <Amt> [0..1] Amount C1 4825
   StartDate <StartDt> [0..1] Date 4825
   EndDate <EndDt> [0..1] Date 4825
66.1.24.14.15  AccumulationRightReference <AcmltnRghtRef>
Presence: [0..1]
Definition: Reference of an accumulation rights program, in which sales commissions are based on a
customer's present purchases of shares and the aggregate quantity previously purchased by the
customer. An accumulation rights program is mainly used in the US market.
Datatype: "Max35Text" on page 5403
66.1.24.14.16  RequiredSignatoriesNumber <ReqrdSgntriesNb>
Presence: [0..1]
Definition: Number of account owners or related parties required to authorise transactions on the
account.
Datatype: "Number" on page 5400
66.1.24.14.17  FundFamilyName <FndFmlyNm>
Presence: [0..1]
Definition: Name of the investment fund family.
Datatype: "Max350Text" on page 5403
66.1.24.14.18  ModifiedFinancialInstrumentDetails <ModfdFinInstrmDtls>
Presence: [0..*]
Definition: Detailed information about the financial instrument associated to the account that is to be
modified or deleted.
ModifiedFinancialInstrumentDetails <ModfdFinInstrmDtls> contains the following
ModificationScope42 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ModificationScopeIndication <ModScpIndctn> [1..1] CodeSet 4653
   FinancialInstrumentDetails <FinInstrmDtls> [1..1] ± C20 4654
66.1.24.14.18.1  ModificationScopeIndication <ModScpIndctn>
Presence: [1..1]
Definition: Type of modification to be applied.
Datatype: "DataModification2Code" on page 5293
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4653 May 2026
```

