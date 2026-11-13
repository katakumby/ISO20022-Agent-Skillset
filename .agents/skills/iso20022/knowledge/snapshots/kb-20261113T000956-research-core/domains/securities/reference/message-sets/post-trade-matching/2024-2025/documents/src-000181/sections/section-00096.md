---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.19 OtherBusinessParties <OthrBizPties>"]
file_pages: [127]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.19 OtherBusinessParties <OthrBizPties>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 127 to 127.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 127

```text
3.4.19 OtherBusinessParties <OthrBizPties>
Presence: [0..1]
Definition: Other business parties relevant to the transaction.
Impacted by: C26 "InvestorUsageRule", C44 "QualifiedForeignIntermediaryRule"
OtherBusinessParties <OthrBizPties> contains the following OtherParties32 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Investor <Invstr> [0..*] ± C25 127
   StockExchange <StockXchg> [0..1] ± 128
   TradeRegulator <TradRgltr> [0..1] ± 128
   TripartyAgent <TrptyAgt> [0..1] ± 128
   QualifiedForeignIntermediary <QlfdFrgnIntrmy> [0..1] ± 129
Constraints
• InvestorUsageRule
When investor is used with a country code, the country code specifies the nationality of the investor,
for the settlement of certain securities (i.e. airlines, defence manufacturers) under the EU legislation.
• QualifiedForeignIntermediaryRule
If Qualified Foreign Intermediary is used, then the instruction must be a delivery.
3.4.19.1  Investor <Invstr>
Presence: [0..*]
Definition: Party that identifies the underlying investor.
Impacted by: C25 "IdentificationUsageRule"
Investor <Invstr> contains the following elements (see "PartyIdentificationAndAccount150" on
page 399 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 399
   SafekeepingAccount <SfkpgAcct> [0..1] Text 400
   CashAccount <CshAcct> [0..1] ± 400
   ProcessingIdentification <PrcgId> [0..1] Text 400
   CountryOfResidence <CtryOfRes> [0..1] CodeSet C4 401
   AdditionalInformation <AddtlInf> [0..1] ± C2 401
   AlternateIdentification <AltrnId> [0..1] ± 401
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 127 February 2025
```

