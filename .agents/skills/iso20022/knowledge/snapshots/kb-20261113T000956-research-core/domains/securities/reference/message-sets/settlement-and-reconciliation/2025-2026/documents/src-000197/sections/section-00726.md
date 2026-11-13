---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10", "30.4 Message Building Blocks", "30.4.6 SettlementParameters <SttlmParams>", "30.4.6.6 SecuritiesRTGS <SctiesRTGS>"]
file_pages: [1082]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.036.001.10"]
---

# 30.4.6.6 SecuritiesRTGS <SctiesRTGS>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1082 to 1082.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1082

```text
Definition: Specifies the stamp duty type or exemption reason applicable to the settlement transaction.
StampDutyTaxBasis <StmpDtyTaxBsis> contains the following elements (see
"GenericIdentification30" on page 1502 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
30.4.6.6  SecuritiesRTGS <SctiesRTGS>
Presence: [0..1]
Definition: Specifies whether the settlement transaction is to be settled through an RTGS or a non
RTGS system.
SecuritiesRTGS <SctiesRTGS> contains one of the following elements (see
"SecuritiesRTGS4Choice" on page 1554 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 1554
Or}   Proprietary <Prtry> [1..1] ± 1554
30.4.6.7  BeneficialOwnership <BnfclOwnrsh>
Presence: [0..1]
Definition: Specifies whether there is change of beneficial ownership.
BeneficialOwnership <BnfclOwnrsh> contains one of the following elements (see
"BeneficialOwnership4Choice" on page 1600 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 1600
Or}   Proprietary <Prtry> [1..1] ± 1600
30.4.6.8  CashClearingSystem <CshClrSys>
Presence: [0..1]
Definition: Specifies the category of cash clearing system, for example, cheque clearing.
CashClearingSystem <CshClrSys> contains one of the following elements (see
"CashSettlementSystem6Choice" on page 1433 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1433
Or}   Proprietary <Prtry> [1..1] ± 1433
Approved by the Securities SEG on 27 January 2026 sese.036.001.10
SecuritiesFinancingModificationInstructionV10
Settlement And Reconciliation - Maintenance 2025 - 2026 1082 March 2026
```

