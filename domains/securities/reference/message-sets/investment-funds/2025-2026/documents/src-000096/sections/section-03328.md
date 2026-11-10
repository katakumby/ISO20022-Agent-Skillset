---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.3 InvestmentAccount74", "66.1.24.3.18 AccumulationRightReference <AcmltnRghtRef>"]
file_pages: [4567]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.3.18 AccumulationRightReference <AcmltnRghtRef>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4567 to 4567.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4567

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
66.1.24.3.18  AccumulationRightReference <AcmltnRghtRef>
Presence: [0..1]
Definition: Reference of an accumulation rights program, in which sales commissions are based on a
customer's present purchases of shares and the aggregate quantity previously purchased by the
customer. An accumulation rights program is mainly used in the US market.
Datatype: "Max35Text" on page 5403
66.1.24.3.19  RequiredSignatoriesNumber <ReqrdSgntriesNb>
Presence: [0..1]
Definition: Number of account owners or related parties required to authorise transactions on the
account.
Datatype: "Number" on page 5400
66.1.24.3.20  FundFamilyName <FndFmlyNm>
Presence: [0..1]
Definition: Name of the investment fund family.
Datatype: "Max350Text" on page 5403
66.1.24.3.21  FinancialInstrumentDetails <FinInstrmDtls>
Presence: [0..*]
Definition: Detailed information about the investment fund or security associated to the account.
Impacted by: C20 "IdentificationGuideline"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4567 May 2026
```

