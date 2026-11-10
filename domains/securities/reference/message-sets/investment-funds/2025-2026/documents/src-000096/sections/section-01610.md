---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "44.4 Message Building Blocks", "44.4.3 PreviousReference <PrvsRef>", "44.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "44.4.4.9.21 CashSettlementDetails <CshSttlmDtls>", "44.4.4.9.21.1 PaymentInstrument <PmtInstrm>", "44.4.4.9.21.1.3 BankersDraftDetails <BkrsDrftDtls>", "44.4.4.9.21.1.3.4 DrawerIdentification <DrwrId>"]
file_pages: [2247]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.004.001.05"]
---

# 44.4.4.9.21.1.3.4 DrawerIdentification <DrwrId>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2247 to 2247.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2247

```text
Definition: Legal entity identification as an alternate identification for the party.
Datatype: "LEIIdentifier" on page 5395
44.4.4.9.21.1.3.4  DrawerIdentification <DrwrId>
Presence: [0..1]
Definition: Account owner that issues the cheque ordering the drawee bank to pay a specific amount,
upon demand, to the payee.
DrawerIdentification <DrwrId> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
44.4.4.9.21.1.4  CashAccountDetails <CshAcctDtls>
Presence: [1..1]
Definition: Part of the investment account to or from which cash entries are made.
Impacted by: C1 "AccountElementRule"
CashAccountDetails <CshAcctDtls> contains the following InvestmentAccount60 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountIdentification <AcctId> [0..1] Text 2247
   Type <Tp> [0..1] ± 2247
Constraints
• AccountElementRule
Either AccountIdentification or Type must be present. Both may be present.
44.4.4.9.21.1.4.1  AccountIdentification <AcctId>
Presence: [0..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Datatype: "Max35Text" on page 5403
44.4.4.9.21.1.4.2  Type <Tp>
Presence: [0..1]
Definition: Account type.
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2247 May 2026
```

