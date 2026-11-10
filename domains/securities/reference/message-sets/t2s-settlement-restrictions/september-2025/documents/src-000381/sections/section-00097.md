---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01", "5.4 Message Building Blocks", "5.4.3 Modifications <Mods>", "5.4.3.4 Modification <Mod>", "5.4.3.4.7 Underlying <Undrlyg>", "5.4.3.4.7.1 IntraPositionMovement <IntraPosMvmnt>", "5.4.3.4.7.1.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [126]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.031.001.01"]
---

# 5.4.3.4.7.1.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 126 to 126.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 126

```text
IntraPositionMovement <IntraPosMvmnt> contains the following IntraPosition6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C11,
C12,
C13,
C14,
C16
126
   SettlementQuantity <SttlmQty> [1..1] ± 127
   SettlementDate <SttlmDt> [1..1] ± 127
   BalanceFrom <BalFr> [0..1] ± 127
   BalanceTo <BalTo> [0..1] ± 128
   SecuritiesSubBalanceIdentification <SctiesSubBalId> [0..1] ± 128
   Priority <Prty> [0..1] ± 128
5.4.3.4.7.1.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instruments representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C11 "DescriptionPresenceRule", C12 "DescriptionUsageRule", C13 "ISINGuideline", C14
"ISINPresenceRule", C16 "OtherIdentificationPresenceRule"
FinancialInstrumentIdentification <FinInstrmId> contains the following elements (see
"SecurityIdentification19" on page 207 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 208
   OtherIdentification <OthrId> [0..*]  208
     Identification <Id> [1..1] Text 208
     Suffix <Sfx> [0..1] Text 208
     Type <Tp> [1..1] ± 208
   Description <Desc> [0..1] Text 208
Constraints
• DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification must be
present.
On Condition
    /Description is absent
Following Must be True
    /ISIN Must be present
 Or    /OtherIdentification[*] Must be present
• DescriptionUsageRule
Description must be used alone as the last resort.
Approved by the Securities SEG on 21 August 2025 semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities - Settlement Restrictions 126 September 2025
```

