---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["6 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "6.4 Message Building Blocks", "6.4.6 Penalty <Pnlty>", "6.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "6.4.6.11.1 AccountServicer <AcctSvcr>"]
file_pages: [205]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 6.4.6.11.1 AccountServicer <AcctSvcr>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 205 to 205.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 205

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           EffectiveTime <FctvTm> [0..1] DateTime 243
           StartTime <StartTm> [0..1] DateTime 243
           EndTime <EndTm> [0..1] DateTime 243
       NetMovementDetails <NetMvmntDtls> [0..1]  243
         SafekeepingAccount <SfkpgAcct> [0..1] ± 244
         SecuritiesShortfall <SctiesShrtfll> [0..1] ± 244
         ShortfallValuation <ShrtfllValtn> [0..1] ± 244
         TradeTransactionCondition <TradTxCond> [0..*] ± 245
         NumberOfEntries <NbOfNtries> [0..1] Quantity 245
6.4.6.11.1  AccountServicer <AcctSvcr>
Presence: [0..1]
Definition: Party that manages the sub-level account on behalf of the account owner, that is manages
the registration and booking of entries on the account, calculates balances on the account and provides
information about the account.
AccountServicer <AcctSvcr> contains the following elements (see "PartyIdentification136" on
page 413 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 414
   LEI <LEI> [0..1] IdentifierSet 414
6.4.6.11.2  PartyIdentification <PtyId>
Presence: [1..1]
Definition: Unique identification of the party within the system.
PartyIdentification <PtyId> contains the following PenaltyPartyIdentification1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 205
   Type <Tp> [0..1]  206
{Or     Code <Cd> [1..1] CodeSet 206
Or}     Proprietary <Prtry> [1..1] ± 206
6.4.6.11.2.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the party.
Approved by the Securities SEG 19 February 2026. semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities - Securities and Penalty Reporting 205 March 2026
```

