---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["24 sese.001.001.10 TransferOutInstructionV10", "24.4 Message Building Blocks", "24.4.5 MasterReference <MstrRef>", "24.4.6.1 TransferReference <TrfRef>"]
file_pages: [449]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.001.001.10"]
---

# 24.4.6.1 TransferReference <TrfRef>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 449 to 449.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 449

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
             Issuer <Issr> [1..1] Text 480
             SchemeName <SchmeNm> [0..1] Text 480
         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 480
     OtherAmount <OthrAmt> [0..*]  480
       Type <Tp> [1..1]  481
{Or         Code <Cd> [1..1] CodeSet 481
Or}         ProprietaryCode <PrtryCd> [1..1] ± 481
       Amount <Amt> [1..1] Amount C1, C10 481
   Rounding <Rndg> [0..1] CodeSet 482
   OriginalCost <OrgnlCost> [0..1] Amount C1 482
   AveragePrice <AvrgPric> [0..1] Amount C2 482
   TransferCurrency <TrfCcy> [0..1] CodeSet C2 483
   OwnAccountTransferIndicator <OwnAcctTrfInd> [0..1] Indicator 483
   NonStandardSettlementInformation <NonStdSttlmInf> [0..1] Text 483
   TransferExpensesPaymentType <TrfExpnssPmtTp> [0..1] ± 483
Constraints
• TotalUnitsNumberRule
Quantity/TotalUnitsNumber must be the sum of all occurrences of UnitsDetails/UnitsNumber when
UnitsDetails is present.
24.4.6.1  TransferReference <TrfRef>
Presence: [1..1]
Definition: Unique and unambiguous identifier for the transfer instruction, as assigned by the instructing
party.
Datatype: "Max35Text" on page 5403
24.4.6.2  ClientReference <ClntRef>
Presence: [0..1]
Definition: Unique and unambiguous investor's identification of the transfer. This reference can typically
be used in a hub scenario to give the reference of the transfer as assigned by the underlying client.
Approved by the Securities SEG on 27 January 2026 sese.001.001.10 TransferOutInstructionV10
Investment Funds - Maintenance 2025 - 2026 449 May 2026
```

