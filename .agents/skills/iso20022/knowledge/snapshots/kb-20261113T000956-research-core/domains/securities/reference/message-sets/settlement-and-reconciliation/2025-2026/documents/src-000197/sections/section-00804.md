---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["32 sese.038.001.11 SecuritiesSettlementTransactionModificationRequestV11", "32.4 Message Building Blocks", "32.4.2 UpdateType <UpdTp>", "32.4.2.1 Addition <Addtn>", "32.4.2.1.14 OtherBusinessParties <OthrBizPties>", "32.4.2.1.14.1 Investor <Invstr>"]
file_pages: [1209]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.038.001.11"]
---

# 32.4.2.1.14.1 Investor <Invstr>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1209 to 1209.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1209

```text
OtherBusinessParties <OthrBizPties> contains the following OtherParties43 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Investor <Invstr> [0..*] ± C25,
C60,
C66
1209
   QualifiedForeignIntermediary <QlfdFrgnIntrmy> [0..1] ± C61,
C67
1210
   StockExchange <StockXchg> [0..1] ± 1211
   TradeRegulator <TradRgltr> [0..1] ± 1211
   TripartyAgent <TrptyAgt> [0..1] ± C61,
C67
1211
   Broker <Brkr> [0..1] ± C61,
C67
1212
Constraints
• InvestorCountryCodeRule
If Investor is used with a country code, then the country code specifies the nationality of the investor,
for example, for the settlement of certain securities (that is, airlines, defence manufacturers) under
the EU legislation.
• QualifiedForeignIntermediaryRule
If Qualified Foreign Intermediary is used, then the instruction must be a delivery.
32.4.2.1.14.1  Investor <Invstr>
Presence: [0..*]
Definition: Party, either an individual or organisation, whose assets are being invested.
Impacted by: C25 "IdentificationNationalityOfInvestorRule", C60
"SafekeepingAccountOrBlockChainAddress1Rule", C66
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
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1209 March 2026
```

