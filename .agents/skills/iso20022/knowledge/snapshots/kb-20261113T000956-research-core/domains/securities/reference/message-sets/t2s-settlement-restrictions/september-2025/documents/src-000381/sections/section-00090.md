---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01", "5.4 Message Building Blocks", "5.4.3 Modifications <Mods>", "5.4.3.4 Modification <Mod>", "5.4.3.4.6 RequestDetails <ReqDtls>", "5.4.3.4.6.6 Priority <Prty>"]
file_pages: [119]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.031.001.01"]
---

# 5.4.3.4.6.6 Priority <Prty>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 119 to 119.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 119

```text
Definition: Specifies the type of linkage requested.
Linkage <Lkg> contains one of the following elements (see "LinkageType3Choice" on page 227 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 227
Or}   Proprietary <Prtry> [1..1] ± 228
5.4.3.4.6.6  Priority <Prty>
Presence: [0..1]
Definition: Specifies whether the transaction is to be executed with a high priority.
Priority <Prty> contains one of the following elements (see "PriorityNumeric4Choice" on page 230 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Numeric <Nmrc> [1..1] Text 230
Or}   Proprietary <Prtry> [1..1] ± 230
5.4.3.4.6.7  OtherProcessing <OthrPrcg>
Presence: [0..*]
Definition: Specifies another type of processing change request.
OtherProcessing <OthrPrcg> contains the following elements (see "GenericIdentification30" on
page 224 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 224
   Issuer <Issr> [1..1] Text 224
   SchemeName <SchmeNm> [0..1] Text 224
5.4.3.4.6.8  PartialSettlementIndicator <PrtlSttlmInd>
Presence: [0..1]
Definition: Specifies whether partial settlement is allowed.
Datatype: "SettlementTransactionCondition5Code" on page 339
CodeName Name Definition
PART PartialAllowed Partial settlement is allowed.
NPAR PartialNotAllowed Partial settlement is not allowed.
PARC PartialSettlementCashThresholdAllowed Partial settlement is allowed but must
satisfy a cash value minimum (value
defined in static data).
Approved by the Securities SEG on 21 August 2025 semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities - Settlement Restrictions 119 September 2025
```

