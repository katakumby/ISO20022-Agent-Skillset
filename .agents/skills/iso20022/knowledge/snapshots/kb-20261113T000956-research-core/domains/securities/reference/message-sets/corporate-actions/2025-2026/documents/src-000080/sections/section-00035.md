---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.8 AccountDetails <AcctDtls>", "3.4.8.1 ForAllAccounts <ForAllAccts>"]
file_pages: [75]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.8.1 ForAllAccounts <ForAllAccts>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 75 to 75.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 75

```text
AccountDetails <AcctDtls> contains one of the following AccountIdentification71Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ForAllAccounts <ForAllAccts> [1..1] ± 75
Or}   AccountsListAndBalanceDetails
<AcctsListAndBalDtls>
[1..*]  C101,
C102,
C103,
C104
76
     SafekeepingAccount <SfkpgAcct> [0..1] Text 78
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] Text 78
     AccountOwner <AcctOwnr> [0..1] ± 78
     SafekeepingPlace <SfkpgPlc> [0..1] ± 78
     Balance <Bal> [0..1]  C9 79
       TotalEligibleBalance <TtlElgblBal> [0..1] ± 80
       BlockedBalance <BlckdBal> [0..1] ± 81
       BorrowedBalance <BrrwdBal> [0..1] ± 81
       CollateralInBalance <CollInBal> [0..1] ± 81
       CollateralOutBalance <CollOutBal> [0..1] ± 82
       OnLoanBalance <OnLnBal> [0..1] ± 82
       PendingDeliveryBalance <PdgDlvryBal> [0..*] ± 82
       PendingReceiptBalance <PdgRctBal> [0..*] ± 83
       OutForRegistrationBalance <OutForRegnBal> [0..1] ± 83
       SettlementPositionBalance <SttlmPosBal> [0..*] ± 83
       StreetPositionBalance <StrtPosBal> [0..1] ± 84
       TradeDatePositionBalance <TradDtPosBal> [0..1] ± 84
       InTransshipmentBalance <InTrnsShipmntBal> [0..1] ± 84
       RegisteredBalance <RegdBal> [0..1] ± 85
       ObligatedBalance <OblgtdBal> [0..1] ± 85
       UninstructedBalance <UinstdBal> [0..1] ± 85
       InstructedBalance <InstdBal> [0..1] ± 86
       AffectedBalance <AfctdBal> [0..1] ± 86
       UnaffectedBalance <UafctdBal> [0..1] ± 86
3.4.8.1  ForAllAccounts <ForAllAccts>
Presence: [1..1]
Definition: All safekeeping accounts that own an underlying financial instrument.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 75 February 2026
```

