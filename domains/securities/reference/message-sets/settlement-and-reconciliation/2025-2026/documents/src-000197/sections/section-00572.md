---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11", "26.4 Message Building Blocks", "26.4.14 DigitalPaymentSettlement <DgtlPmtSttlm>", "26.4.15.1 Investor <Invstr>"]
file_pages: [864]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.032.001.13"]
---

# 26.4.15.1 Investor <Invstr>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 864 to 864.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 864

```text
OtherBusinessParties <OthrBizPties> contains the following OtherParties43 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Investor <Invstr> [0..*] ± C30,
C53,
C57
864
   QualifiedForeignIntermediary <QlfdFrgnIntrmy> [0..1] ± C54,
C58
865
   StockExchange <StockXchg> [0..1] ± 866
   TradeRegulator <TradRgltr> [0..1] ± 866
   TripartyAgent <TrptyAgt> [0..1] ± C54,
C58
866
   Broker <Brkr> [0..1] ± C54,
C58
867
Constraints
• InvestorCountryCodeRule
If Investor is used with a country code, then the country code specifies the nationality of the investor,
for example, for the settlement of certain securities (that is, airlines, defence manufacturers) under
the EU legislation.
• QualifiedForeignIntermediaryRule
If Qualified Foreign Intermediary is used, then the instruction must be a delivery.
26.4.15.1  Investor <Invstr>
Presence: [0..*]
Definition: Party, either an individual or organisation, whose assets are being invested.
Impacted by: C30 "IdentificationNationalityOfInvestorRule", C53
"SafekeepingAccountOrBlockChainAddress1Rule", C57
"SafekeepingAccountOrBlockChainAddress2Rule"
Investor <Invstr> contains the following elements (see "PartyIdentificationAndAccount197" on
page 1672 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 1673
   LEI <LEI> [0..1] IdentifierSet 1673
   AlternateIdentification <AltrnId> [0..1] ± 1673
   Nationality <Ntlty> [0..1] CodeSet C7 1674
   SafekeepingAccount <SfkpgAcct> [0..1] Text 1674
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] Text 1674
   ProcessingIdentification <PrcgId> [0..1] Text 1674
   AdditionalInformation <AddtlInf> [0..1] ± C5 1674
Approved by the Securities SEG on 27 January 2026 sese.032.001.13
SecuritiesSettlementTransactionGenerationNotificati
onV13
Settlement And Reconciliation - Maintenance 2025 - 2026 864 March 2026
```

