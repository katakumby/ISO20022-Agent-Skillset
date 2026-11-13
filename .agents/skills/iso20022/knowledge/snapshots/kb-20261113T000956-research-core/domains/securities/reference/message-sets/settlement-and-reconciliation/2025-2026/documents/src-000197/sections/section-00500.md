---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12", "22.4 Message Building Blocks", "22.4.17 OtherBusinessParties <OthrBizPties>", "22.4.17.1 Investor <Invstr>"]
file_pages: [764]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.028.001.12"]
---

# 22.4.17.1 Investor <Invstr>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 764 to 764.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 764

```text
OtherBusinessParties <OthrBizPties> contains the following OtherParties34 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Investor <Invstr> [0..1] ± 764
   QualifiedForeignIntermediary <QlfdFrgnIntrmy> [0..1] ± 764
   StockExchange <StockXchg> [0..1] ± 765
   TradeRegulator <TradRgltr> [0..1] ± 765
   TripartyAgent <TrptyAgt> [0..1] ± 765
Constraints
• InvestorCountryCodeRule
If Investor is used with a country code, then the country code specifies the nationality of the investor,
for example, for the settlement of certain securities (that is, airlines, defence manufacturers) under
the EU legislation.
22.4.17.1  Investor <Invstr>
Presence: [0..1]
Definition: Party, either an individual or organisation, whose assets are being invested.
Investor <Invstr> contains the following elements (see "PartyIdentification149" on page 1687 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  1687
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C5 1687
Or     ProprietaryIdentification <PrtryId> [1..1] ± 1687
Or     NameAndAddress <NmAndAdr> [1..1] ± 1688
Or}     Country <Ctry> [1..1] CodeSet C7 1688
   LEI <LEI> [0..1] IdentifierSet 1688
22.4.17.2  QualifiedForeignIntermediary <QlfdFrgnIntrmy>
Presence: [0..1]
Definition: Foreign financial institution which has been authorised by local authorities to act as account
management institution in the country.
QualifiedForeignIntermediary <QlfdFrgnIntrmy> contains the following elements (see
"PartyIdentification136" on page 1671 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1672
   LEI <LEI> [0..1] IdentifierSet 1672
Approved by the Securities SEG on 27 January 2026 sese.028.001.12
SecuritiesSettlementTransactionAllegementNotificat
ionV12
Settlement And Reconciliation - Maintenance 2025 - 2026 764 March 2026
```

