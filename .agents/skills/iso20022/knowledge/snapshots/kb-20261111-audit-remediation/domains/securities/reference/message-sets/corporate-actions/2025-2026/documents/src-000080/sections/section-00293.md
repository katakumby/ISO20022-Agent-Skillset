---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.11 AccountDetails <AcctDtls>", "7.4.11.1 ForAllAccounts <ForAllAccts>"]
file_pages: [403]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.11.1 ForAllAccounts <ForAllAccts>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 403 to 403.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 403

```text
AccountDetails <AcctDtls> contains one of the following AccountIdentification70Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ForAllAccounts <ForAllAccts> [1..1] ± 403
Or}   AccountsListAndBalanceDetails
<AcctsListAndBalDtls>
[1..*]  C68,
C69,
C70,
C71
404
     SafekeepingAccount <SfkpgAcct> [0..1] Text 406
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] Text 406
     AccountOwner <AcctOwnr> [0..1] ± 406
     SafekeepingPlace <SfkpgPlc> [0..1] ± 406
     Balance <Bal> [0..1]  C7 407
       TotalEligibleBalance <TtlElgblBal> [0..1] ± 408
       BlockedBalance <BlckdBal> [0..1] ± 409
       BorrowedBalance <BrrwdBal> [0..1] ± 409
       CollateralInBalance <CollInBal> [0..1] ± 409
       CollateralOutBalance <CollOutBal> [0..1] ± 410
       OnLoanBalance <OnLnBal> [0..1] ± 410
       PendingDeliveryBalance <PdgDlvryBal> [0..*] ± 410
       PendingReceiptBalance <PdgRctBal> [0..*] ± 411
       OutForRegistrationBalance <OutForRegnBal> [0..1] ± 411
       SettlementPositionBalance <SttlmPosBal> [0..*] ± 411
       StreetPositionBalance <StrtPosBal> [0..1] ± 412
       TradeDatePositionBalance <TradDtPosBal> [0..1] ± 412
       InTransshipmentBalance <InTrnsShipmntBal> [0..1] ± 412
       RegisteredBalance <RegdBal> [0..1] ± 413
       ObligatedBalance <OblgtdBal> [0..1] ± 413
       UninstructedBalance <UinstdBal> [0..1] ± 413
       InstructedBalance <InstdBal> [0..1] ± 414
       AffectedBalance <AfctdBal> [0..1] ± 414
       UnaffectedBalance <UafctdBal> [0..1] ± 414
7.4.11.1  ForAllAccounts <ForAllAccts>
Presence: [1..1]
Definition: All safekeeping accounts that own an underlying financial instrument.
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 403 February 2026
```

