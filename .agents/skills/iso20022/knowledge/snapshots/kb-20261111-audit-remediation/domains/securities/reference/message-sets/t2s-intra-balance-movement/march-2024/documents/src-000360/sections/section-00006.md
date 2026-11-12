---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["2 camt.066.001.02 IntraBalanceMovementInstructionV02", "2.3 Constraints"]
file_pages: [13, 14]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.066.001.02"]
topic_continuations: [{"constraint_ids": ["C14", "C15", "C16", "C17"], "until_heading": "2.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 15, "topic": "2.3 Constraints", "reference_path": "domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00007.md"}]
---

# 2.3 Constraints

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 13 to 14.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 2.3 Constraints topic continues in [Constraints continuation C14–C17 (file p15)](section-00007.md#file-page-15). Read the text before **2.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 13

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       Type <Tp> [1..1]  24
{Or         Code <Cd> [1..1] CodeSet 25
Or}         Proprietary <Prtry> [1..1] ± 25
       QuantityBreakdown <QtyBrkdwn> [0..*]  25
         LotNumber <LotNb> [0..1] ± 25
         LotAmount <LotAmt> [0..1] ± 26
         LotQuantity <LotQty> [0..1] ± 26
         CashSubBalanceType <CshSubBalTp> [0..1] ± 26
     BalanceTo <BalTo> [1..1]  27
       Type <Tp> [1..1]  27
{Or         Code <Cd> [1..1] CodeSet 27
Or}         Proprietary <Prtry> [1..1] ± 27
       QuantityBreakdown <QtyBrkdwn> [0..*]  28
         LotNumber <LotNb> [0..1] ± 28
         LotAmount <LotAmt> [0..1] ± 28
         LotQuantity <LotQty> [0..1] ± 29
         CashSubBalanceType <CshSubBalTp> [0..1] ± 29
     CashSubBalanceIdentification <CshSubBalId> [0..1] ± 29
     Priority <Prty> [0..1] ± 29
     InstructionProcessingAdditionalDetails <InstrPrcgAddtlDtls> [0..1] Text 30
   SupplementaryData <SplmtryData> [0..*] ± C16 30
2.3 Constraints
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
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.066.001.02
IntraBalanceMovementInstructionV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
13 March 2024
```

## File page 14

```text
C3 AdditionalDetailsRule
Unless bilaterally agreed between the sender and the receiver, if
InstructionProcessingAdditionalDetails is present, then it must not contain information that can
be provided in a structured field.
C4 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C5 BalanceFromToRule
The cash balance type of BalanceFrom must be different from the cash balance type of
BalanceTo.
C6 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C7 BlockTradeGuideline
In a block trade instruction, the total number of children must be provided using
TotalOfLinkedInstructions.
The CurrentInstructionNumber of the parent must be 000. The children must have an
incremental CurrentInstructionNumber from 001 to 999.
For more details, see the relevant market practice document on www.smpg.info.
C8 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C9 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C10 CurrentInstructionNumberRule
If the Sender wants to indicate that this instruction is linked to one or more settlement
instruction, then the CurrentInstructionNumber must be specified.
C11 CurrentInstructionNumberRule
If the Sender wants to indicate that this instruction is linked to one or more settlement
instruction, then the CurrentInstructionNumber must be specified.
C12 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C13 IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.066.001.02
IntraBalanceMovementInstructionV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
14 March 2024
```

