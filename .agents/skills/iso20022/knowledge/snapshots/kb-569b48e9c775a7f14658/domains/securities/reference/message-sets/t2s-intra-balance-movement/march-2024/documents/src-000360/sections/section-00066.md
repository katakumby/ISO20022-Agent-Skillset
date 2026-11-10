---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["5 camt.072.001.02 IntraBalanceMovementModificationRequestV02", "5.4 Message Building Blocks", "5.4.5 RequestDetails <ReqDtls>", "5.4.5.7 Linkages <Lnkgs>", "5.4.5.7.3 Reference <Ref>", "5.4.5.7.3.1 SecuritiesSettlementTransactionIdentification <SctiesSttlmTxId>"]
file_pages: [80]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.072.001.02"]
---

# 5.4.5.7.3.1 SecuritiesSettlementTransactionIdentification <SctiesSttlmTxId>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 80 to 80.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 80

```text
Reference <Ref> contains one of the following References34Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 80
Or   IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 80
Or   IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 80
Or   AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 80
Or   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 80
Or   PoolIdentification <PoolId> [1..1] Text 81
Or}   OtherTransactionIdentification <OthrTxId> [1..1] Text 81
5.4.5.7.3.1  SecuritiesSettlementTransactionIdentification <SctiesSttlmTxId>
Presence: [1..1]
Definition: Unambiguous identification of a securities settlement transaction as known by the account
owner (or instructing party acting on its behalf).
Datatype: "Max35Text" on page 497
5.4.5.7.3.2  IntraPositionMovementIdentification <IntraPosMvmntId>
Presence: [1..1]
Definition: Unambiguous identification of the intra-position movement transaction as known by the
account owner (or instructing party acting on its behalf).
Datatype: "Max35Text" on page 497
5.4.5.7.3.3  IntraBalanceMovementIdentification <IntraBalMvmntId>
Presence: [1..1]
Definition: Unambiguous identification of the intra-balance movement transaction as known by the
account owner (or instructing party acting on its behalf).
Datatype: "Max35Text" on page 497
5.4.5.7.3.4  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 497
5.4.5.7.3.5  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [1..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 497
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.072.001.02
IntraBalanceMovementModificationRequestV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
80 March 2024
```

