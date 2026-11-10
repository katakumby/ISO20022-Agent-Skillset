---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01", "5.4 Message Building Blocks", "5.4.3 Modifications <Mods>", "5.4.3.4 Modification <Mod>", "5.4.3.4.6 RequestDetails <ReqDtls>", "5.4.3.4.6.13 Linkages <Lnkgs>", "5.4.3.4.6.13.3 Reference <Ref>", "5.4.3.4.6.13.3.1 SecuritiesSettlementTransactionIdentification <SctiesSttlmTxId>"]
file_pages: [123]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.031.001.01"]
---

# 5.4.3.4.6.13.3.1 SecuritiesSettlementTransactionIdentification <SctiesSttlmTxId>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 123 to 123.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 123

```text
Reference <Ref> contains one of the following References34Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 123
Or   IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 123
Or   IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 123
Or   AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 123
Or   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 123
Or   PoolIdentification <PoolId> [1..1] Text 124
Or}   OtherTransactionIdentification <OthrTxId> [1..1] Text 124
5.4.3.4.6.13.3.1  SecuritiesSettlementTransactionIdentification <SctiesSttlmTxId>
Presence: [1..1]
Definition: Unambiguous identification of a securities settlement transaction as known by the account
owner (or instructing party acting on its behalf).
Datatype: "Max35Text" on page 345
5.4.3.4.6.13.3.2  IntraPositionMovementIdentification <IntraPosMvmntId>
Presence: [1..1]
Definition: Unambiguous identification of the intra-position movement transaction as known by the
account owner (or instructing party acting on its behalf).
Datatype: "Max35Text" on page 345
5.4.3.4.6.13.3.3  IntraBalanceMovementIdentification <IntraBalMvmntId>
Presence: [1..1]
Definition: Unambiguous identification of the intra-balance movement transaction as known by the
account owner (or instructing party acting on its behalf).
Datatype: "Max35Text" on page 345
5.4.3.4.6.13.3.4  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 345
5.4.3.4.6.13.3.5  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [1..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 345
Approved by the Securities SEG on 21 August 2025 semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities - Settlement Restrictions 123 September 2025
```

