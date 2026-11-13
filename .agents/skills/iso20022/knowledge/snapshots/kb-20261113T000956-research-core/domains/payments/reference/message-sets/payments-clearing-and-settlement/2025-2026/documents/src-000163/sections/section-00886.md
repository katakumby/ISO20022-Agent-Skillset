---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.8 Frequency", "10.1.8.1 Frequency36Choice", "10.1.8.1.3 PointInTime <PtInTm>", "10.1.8.1.3.2 PointInTime <PtInTm>"]
file_pages: [1181]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.8.1.3.2 PointInTime <PtInTm>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1181 to 1181.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1181

```text
CodeName Name Definition
YEAR Annual Event takes place every year or once a
year.
MNTH Monthly Event takes place every month or once a
month.
QURT Quarterly Event takes place every three months or
four times a year.
MIAN SemiAnnual Event takes place every six months or
two times a year.
WEEK Weekly Event takes place once a week.
DAIL Daily Event takes place every day.
ADHO Adhoc Event takes place on request or as
necessary.
INDA IntraDay Event takes place several times a day.
FRTN Fortnightly Event takes place every two weeks.
10.1.8.1.3.2  PointInTime <PtInTm>
Presence: [1..1]
Definition: Further information on the exact point in time the event should take place.
Datatype: "Exact2NumericText" on page 1243
10.1.9 Identification Information
10.1.9.1  References80Choice
Definition: Choice between references.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 1182
Or   IntraPositionMovementIdentification <IntraPosMvmntId> [1..1] Text 1182
Or   IntraBalanceMovementIdentification <IntraBalMvmntId> [1..1] Text 1182
Or   AccountServicerTransactionIdentification <AcctSvcrTxId> [1..1] Text 1182
Or   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 1182
Or   CounterpartyMarketInfrastructureTransactionIdentificatio
n <CtrPtyMktInfrstrctrTxId>
[1..1] Text 1182
Or   PoolIdentification <PoolId> [1..1] Text 1182
Or   CommonIdentification <CmonId> [1..1] Text 1182
Or   TradeIdentification <TradId> [1..1] Text 1183
Or   UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 1183
Or}   OtherTransactionIdentification <OthrTxId> [1..1] Text 1183
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1181 March 2026
```

