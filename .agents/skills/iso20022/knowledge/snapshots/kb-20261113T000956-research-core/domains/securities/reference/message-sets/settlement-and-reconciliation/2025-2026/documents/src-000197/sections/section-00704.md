---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["29 sese.035.001.13 SecuritiesFinancingConfirmationV13", "29.4 Message Building Blocks", "29.4.16 OtherBusinessParties <OthrBizPties>", "29.4.16.1 Investor <Invstr>"]
file_pages: [1053]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.035.001.13"]
---

# 29.4.16.1 Investor <Invstr>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1053 to 1053.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1053

```text
OtherBusinessParties <OthrBizPties> contains the following OtherParties43 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Investor <Invstr> [0..*] ± C22,
C41,
C45
1053
   QualifiedForeignIntermediary <QlfdFrgnIntrmy> [0..1] ± C42,
C46
1054
   StockExchange <StockXchg> [0..1] ± 1055
   TradeRegulator <TradRgltr> [0..1] ± 1055
   TripartyAgent <TrptyAgt> [0..1] ± C42,
C46
1055
   Broker <Brkr> [0..1] ± C42,
C46
1056
Constraints
• InvestorCountryCodeRule
If Investor is used with a country code, then the country code specifies the nationality of the investor,
for example, for the settlement of certain securities (that is, airlines, defence manufacturers) under
the EU legislation.
• QualifiedForeignIntermediaryRule
If Qualified Foreign Intermediary is used, then the instruction must be a delivery.
29.4.16.1  Investor <Invstr>
Presence: [0..*]
Definition: Party, either an individual or organisation, whose assets are being invested.
Impacted by: C22 "IdentificationNationalityOfInvestorRule", C41
"SafekeepingAccountOrBlockChainAddress1Rule", C45
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
Approved by the Securities SEG on 27 January 2026 sese.035.001.13
SecuritiesFinancingConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 1053 March 2026
```

