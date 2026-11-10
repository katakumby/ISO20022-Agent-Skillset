---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12", "20.4 Message Building Blocks", "20.4.15 DigitalPaymentSettlement <DgtlPmtSttlm>", "20.4.16.1 Investor <Invstr>"]
file_pages: [701]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.026.001.12"]
---

# 20.4.16.1 Investor <Invstr>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 701 to 701.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 701

```text
Definition: Other business parties relevant to the transaction.
Impacted by: C24 "InvestorCountryCodeRule", C39 "QualifiedForeignIntermediaryRule"
OtherBusinessParties <OthrBizPties> contains the following OtherParties43 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Investor <Invstr> [0..*] ± C22,
C43,
C47
701
   QualifiedForeignIntermediary <QlfdFrgnIntrmy> [0..1] ± C44,
C48
702
   StockExchange <StockXchg> [0..1] ± 703
   TradeRegulator <TradRgltr> [0..1] ± 703
   TripartyAgent <TrptyAgt> [0..1] ± C44,
C48
704
   Broker <Brkr> [0..1] ± C44,
C48
705
Constraints
• InvestorCountryCodeRule
If Investor is used with a country code, then the country code specifies the nationality of the investor,
for example, for the settlement of certain securities (that is, airlines, defence manufacturers) under
the EU legislation.
• QualifiedForeignIntermediaryRule
If Qualified Foreign Intermediary is used, then the instruction must be a delivery.
20.4.16.1  Investor <Invstr>
Presence: [0..*]
Definition: Party, either an individual or organisation, whose assets are being invested.
Impacted by: C22 "IdentificationNationalityOfInvestorRule", C43
"SafekeepingAccountOrBlockChainAddress1Rule", C47
"SafekeepingAccountOrBlockChainAddress2Rule"
Approved by the Securities SEG on 27 January 2026 sese.026.001.12
SecuritiesSettlementTransactionReversalAdviceV12
Settlement And Reconciliation - Maintenance 2025 - 2026 701 March 2026
```

