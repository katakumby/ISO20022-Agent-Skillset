---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["25 sese.002.001.09 TransferOutCancellationRequestV09", "26.4 Message Building Blocks", "26.4.6 TransferDetails <TrfDtls>", "26.4.6.1 TransferConfirmationReference <TrfConfRef>"]
file_pages: [536]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.003.001.10"]
---

# 26.4.6.1 TransferConfirmationReference <TrfConfRef>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 536 to 536.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 536

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
             Quantity <Qty> [1..1] Quantity 568
             QuantityType <QtyTp> [1..1] Text 568
             Issuer <Issr> [1..1] Text 568
             SchemeName <SchmeNm> [0..1] Text 568
         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 568
     OtherAmount <OthrAmt> [0..*]  568
       Type <Tp> [1..1]  569
{Or         Code <Cd> [1..1] CodeSet 569
Or}         ProprietaryCode <PrtryCd> [1..1] ± 569
       Amount <Amt> [1..1] Amount C1, C10 569
   Rounding <Rndg> [0..1] CodeSet 570
   OriginalCost <OrgnlCost> [0..1] Amount C1 570
   AveragePrice <AvrgPric> [0..1] Amount C2 570
   NewAveragePrice <NewAvrgPric> [0..1] Amount C2 571
   AverageDate <AvrgDt> [0..1] Date 571
   NewAverageDate <NewAvrgDt> [0..1] Date 571
   TransferCurrency <TrfCcy> [0..1] CodeSet C2 571
   OwnAccountTransferIndicator <OwnAcctTrfInd> [0..1] Indicator 572
   NonStandardSettlementInformation <NonStdSttlmInf> [0..1] Text 572
   TransferExpensesPaymentType <TrfExpnssPmtTp> [0..1] ± 572
Constraints
• TotalUnitsNumberRule
TotalUnitsNumber must be the sum of all occurrences of UnitsDetails/UnitsNumber when
UnitsDetails is present.
26.4.6.1  TransferConfirmationReference <TrfConfRef>
Presence: [1..1]
Definition: Unique and unambiguous identifier for the transfer execution, as assigned by the confirming
party.
Datatype: "Max35Text" on page 5403
26.4.6.2  TransferReference <TrfRef>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 sese.003.001.10 TransferOutConfirmationV10
Investment Funds - Maintenance 2025 - 2026 536 May 2026
```

