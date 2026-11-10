---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.10 AccountDetails <AcctDtls>"]
file_pages: [564]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.10 AccountDetails <AcctDtls>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 564 to 564.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 564

```text
Constraints
• DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token identifier.
8.4.10 AccountDetails <AcctDtls>
Presence: [1..1]
Definition: General information about the safekeeping account, owner and account balance.
Impacted by: C53 "SafekeepingAccountOrBlockChainAddress1Rule", C55
"SafekeepingAccountOrBlockChainAddress2Rule", C57
"SafekeepingAccountOrBlockChainAddress3Rule", C59 "SafekeepingPlaceRule"
AccountDetails <AcctDtls> contains the following AccountAndBalance58 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingAccount <SfkpgAcct> [0..1] Text 565
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] Text 565
   AccountOwner <AcctOwnr> [0..1] ± 565
   SafekeepingPlace <SfkpgPlc> [0..1] ± 566
   Balance <Bal> [1..1]  C7 566
     ConfirmedBalance <ConfdBal> [1..1] ± 567
     TotalEligibleBalance <TtlElgblBal> [0..1] ± 568
     BlockedBalance <BlckdBal> [0..1] ± 568
     BorrowedBalance <BrrwdBal> [0..1] ± 568
     CollateralInBalance <CollInBal> [0..1] ± 568
     CollateralOutBalance <CollOutBal> [0..1] ± 569
     OnLoanBalance <OnLnBal> [0..1] ± 569
     PendingDeliveryBalance <PdgDlvryBal> [0..*] ± 569
     PendingReceiptBalance <PdgRctBal> [0..*] ± 570
     OutForRegistrationBalance <OutForRegnBal> [0..1] ± 570
     SettlementPositionBalance <SttlmPosBal> [0..*] ± 570
     StreetPositionBalance <StrtPosBal> [0..1] ± 571
     TradeDatePositionBalance <TradDtPosBal> [0..1] ± 571
     InTransshipmentBalance <InTrnsShipmntBal> [0..1] ± 571
     RegisteredBalance <RegdBal> [0..1] ± 572
     AffectedBalance <AfctdBal> [0..1] ± 572
     UnaffectedBalance <UafctdBal> [0..1] ± 572
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 564 February 2026
```

