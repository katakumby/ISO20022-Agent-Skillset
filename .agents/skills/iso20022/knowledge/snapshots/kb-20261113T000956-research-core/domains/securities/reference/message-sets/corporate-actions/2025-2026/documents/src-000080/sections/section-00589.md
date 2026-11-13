---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["14 seev.042.001.14 CorporateActionInstructionStatementReportV14", "14.4 Message Building Blocks", "14.4.3 AccountAndStatementDetails <AcctAndStmtDtls>", "14.4.3.1 SafekeepingAccount <SfkpgAcct>"]
file_pages: [768]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.042.001.14"]
---

# 14.4.3.1 SafekeepingAccount <SfkpgAcct>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 768 to 768.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 768

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       StreetPositionBalance <StrtPosBal> [0..1] ± 808
       TradeDatePositionBalance <TradDtPosBal> [0..1] ± 808
       InTransshipmentBalance <InTrnsShipmntBal> [0..1] ± 809
       RegisteredBalance <RegdBal> [0..1] ± 809
       ObligatedBalance <OblgtdBal> [0..1] ± 809
       PendingDeliveryBalance <PdgDlvryBal> [0..*]  810
         Balance <Bal> [1..1] ± 810
         PendingTransactions <PdgTxs> [0..*] ± 810
       PendingReceiptBalance <PdgRctBal> [0..*]  810
         Balance <Bal> [1..1] ± 811
         PendingTransactions <PdgTxs> [0..*] ± 811
     SupplementaryData <SplmtryData> [0..*] ± C23 811
Constraints
• SafekeepingAccountOrBlockChainAddress1Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
Following Must be True
    /SafekeepingAccount Must be present
 Or    /BlockChainAddressOrWallet Must be present
• SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present then SafekeepingAccount must be absent.
On Condition
    /BlockChainAddressOrWallet is present
Following Must be True
    /SafekeepingAccount Must be absent
• SafekeepingAccountOrBlockChainAddress3Rule
If SafekeepingAccount is present, then BlockChainAddressOrWallet must be absent.
On Condition
    /SafekeepingAccount is present
Following Must be True
    /BlockChainAddressOrWallet Must be absent
• SafekeepingPlaceRule
SafekeepingPlace is only to be used by global custodians that allow their clients to specify where the
securities are to be held, for example, in an ICSD account versus an account at the local CSD.
14.4.3.1  SafekeepingAccount <SfkpgAcct>
Presence: [0..1]
Definition: Account where financial instruments are maintained.
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 768 February 2026
```

