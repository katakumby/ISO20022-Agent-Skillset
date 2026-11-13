---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["28 camt.050.001.07 LiquidityCreditTransferV07", "28.2 Structure"]
file_pages: [669]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.050.001.07"]
---

# 28.2 Structure

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 669 to 669.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 669

```text
28.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <LqdtyCdtTrf> [1..1]  
   MessageHeader <MsgHdr> [1..1] ± 670
   LiquidityCreditTransfer <LqdtyCdtTrf> [1..1]  C5 670
     LiquidityTransferIdentification <LqdtyTrfId> [0..1]  671
       InstructionIdentification <InstrId> [0..1] Text 671
       EndToEndIdentification <EndToEndId> [1..1] Text 672
       TransactionIdentification <TxId> [0..1] Text 672
       UETR <UETR> [0..1] IdentifierSet 672
     Creditor <Cdtr> [0..1] ± 672
     CreditorAccount <CdtrAcct> [0..1] ± C9, C8 673
     TransferredAmount <TrfdAmt> [1..1] ± 674
     Debtor <Dbtr> [0..1] ± 674
     DebtorAccount <DbtrAcct> [0..1] ± C9, C8 675
     SettlementDate <SttlmDt> [0..1] Date 676
   SupplementaryData <SplmtryData> [0..*] ± C10 676
28.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C3 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C4 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
Approved by the Payments SEG on 04 February 2025 camt.050.001.07 LiquidityCreditTransferV07
Cash Management - Maintenance 2024 - 2025 669 February 2025
```

