---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.11 AccountDetails <AcctDtls>", "7.4.11.2 AccountsListAndBalanceDetails <AcctsListAndBalDtls>"]
file_pages: [404, 405]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.11.2 AccountsListAndBalanceDetails <AcctsListAndBalDtls>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 404 to 405.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 404

```text
ForAllAccounts <ForAllAccts> contains the following elements (see "AccountIdentification10" on
page 830 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IdentificationCode <IdCd> [1..1] CodeSet 830
7.4.11.2  AccountsListAndBalanceDetails <AcctsListAndBalDtls>
Presence: [1..*]
Definition: Selected safekeeping accounts list (and optionally balance information) to which the
corporate action event applies.
Impacted by: C68 "SafekeepingAccountOrBlockChainAddress1Rule", C69
"SafekeepingAccountOrBlockChainAddress2Rule", C70
"SafekeepingAccountOrBlockChainAddress3Rule", C71 "SafekeepingPlaceRule"
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 404 February 2026
```

## File page 405

```text
AccountsListAndBalanceDetails <AcctsListAndBalDtls> contains the following
AccountAndBalance59 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
Constraints
• SafekeepingAccountOrBlockChainAddress1Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
Following Must be True
    /SafekeepingAccount Must be present
 Or    /BlockChainAddressOrWallet Must be present
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 405 February 2026
```

