---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["81 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "81.4 Message Building Blocks", "81.4.6 Penalty <Pnlty>", "81.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "81.4.6.11.1 AccountServicer <AcctSvcr>"]
file_pages: [2787]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 81.4.6.11.1 AccountServicer <AcctSvcr>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2787 to 2787.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2787

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           EffectiveTime <FctvTm> [0..1] DateTime 2825
           StartTime <StartTm> [0..1] DateTime 2825
           EndTime <EndTm> [0..1] DateTime 2825
       NetMovementDetails <NetMvmntDtls> [0..1]  2825
         SafekeepingAccount <SfkpgAcct> [0..1] ± 2826
         SecuritiesShortfall <SctiesShrtfll> [0..1] ± 2826
         ShortfallValuation <ShrtfllValtn> [0..1] ± 2826
         TradeTransactionCondition <TradTxCond> [0..*] ± 2827
         NumberOfEntries <NbOfNtries> [0..1] Quantity 2827
81.4.6.11.1  AccountServicer <AcctSvcr>
Presence: [0..1]
Definition: Party that manages the sub-level account on behalf of the account owner, that is manages
the registration and booking of entries on the account, calculates balances on the account and provides
information about the account.
AccountServicer <AcctSvcr> contains the following elements (see "PartyIdentification136" on
page 3060 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
81.4.6.11.2  PartyIdentification <PtyId>
Presence: [1..1]
Definition: Unique identification of the party within the system.
PartyIdentification <PtyId> contains the following PenaltyPartyIdentification1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 2787
   Type <Tp> [0..1]  2788
{Or     Code <Cd> [1..1] CodeSet 2788
Or}     Proprietary <Prtry> [1..1] ± 2788
81.4.6.11.2.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the party.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2787 August 2026
```

