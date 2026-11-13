---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.21 Status", "9.1.21.3 ProprietaryStatusAndReason6"]
file_pages: [270]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.21.3 ProprietaryStatusAndReason6

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 270 to 270.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 270

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 224 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 224
   Issuer <Issr> [1..1] Text 224
   SchemeName <SchmeNm> [0..1] Text 224
9.1.21.3  ProprietaryStatusAndReason6
Definition: Provides the proprietary status and reason of an instruction or an instruction cancellation.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProprietaryStatus <PrtrySts> [1..1] ± 270
   ProprietaryReason <PrtryRsn> [0..*] ± C5 270
9.1.21.3.1  ProprietaryStatus <PrtrySts>
Presence: [1..1]
Definition: Proprietary identification of the status related to an instruction.
ProprietaryStatus <PrtrySts> contains the following elements (see "GenericIdentification30" on
page 224 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 224
   Issuer <Issr> [1..1] Text 224
   SchemeName <SchmeNm> [0..1] Text 224
9.1.21.3.2  ProprietaryReason <PrtryRsn>
Presence: [0..*]
Definition: Proprietary identification of the reason related to a proprietary status.
Impacted by: C5 "AdditionalReasonInforrmationRule"
ProprietaryReason <PrtryRsn> contains the following elements (see "ProprietaryReason4" on
page 272 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 273
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 273
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 270 September 2025
```

