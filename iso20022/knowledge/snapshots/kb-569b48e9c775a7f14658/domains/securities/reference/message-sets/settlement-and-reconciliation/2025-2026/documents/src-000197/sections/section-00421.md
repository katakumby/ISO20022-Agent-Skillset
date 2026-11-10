---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13", "19.4 Message Building Blocks", "19.4.16 OtherBusinessParties <OthrBizPties>", "19.4.16.1 Investor <Invstr>"]
file_pages: [647]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.025.001.13"]
---

# 19.4.16.1 Investor <Invstr>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 647 to 647.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 647

```text
Definition: Other business parties relevant to the transaction.
Impacted by: C24 "InvestorCountryCodeRule", C40 "QualifiedForeignIntermediaryRule"
OtherBusinessParties <OthrBizPties> contains the following OtherParties43 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Investor <Invstr> [0..*] ± C22,
C44,
C48
647
   QualifiedForeignIntermediary <QlfdFrgnIntrmy> [0..1] ± C45,
C49
648
   StockExchange <StockXchg> [0..1] ± 649
   TradeRegulator <TradRgltr> [0..1] ± 649
   TripartyAgent <TrptyAgt> [0..1] ± C45,
C49
650
   Broker <Brkr> [0..1] ± C45,
C49
651
Constraints
• InvestorCountryCodeRule
If Investor is used with a country code, then the country code specifies the nationality of the investor,
for example, for the settlement of certain securities (that is, airlines, defence manufacturers) under
the EU legislation.
• QualifiedForeignIntermediaryRule
If Qualified Foreign Intermediary is used, then the instruction must be a delivery.
19.4.16.1  Investor <Invstr>
Presence: [0..*]
Definition: Party, either an individual or organisation, whose assets are being invested.
Impacted by: C22 "IdentificationNationalityOfInvestorRule", C44
"SafekeepingAccountOrBlockChainAddress1Rule", C48
"SafekeepingAccountOrBlockChainAddress2Rule"
Approved by the Securities SEG on 27 January 2026 sese.025.001.13
SecuritiesSettlementTransactionConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 647 March 2026
```

