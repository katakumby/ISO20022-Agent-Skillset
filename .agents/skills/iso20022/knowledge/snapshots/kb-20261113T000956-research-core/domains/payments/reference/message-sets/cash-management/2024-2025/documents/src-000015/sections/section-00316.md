---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["11 camt.012.001.08 DeleteLimitV08", "11.4 Message Building Blocks", "11.4.2 LimitDetails <LmtDtls>", "11.4.2.1 CurrentLimitIdentification <CurLmtId>"]
file_pages: [453]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.012.001.08"]
---

# 11.4.2.1 CurrentLimitIdentification <CurLmtId>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 453 to 453.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 453

```text
LimitDetails <LmtDtls> contains one of the following LimitStructure3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   CurrentLimitIdentification <CurLmtId> [1..1]  C2, C3 453
     SystemIdentification <SysId> [0..1] ± 454
     BilateralLimitCounterpartyIdentification
<BilLmtCtrPtyId>
[0..1] ± 454
     Type <Tp> [1..1]  455
{Or       Code <Cd> [1..1] CodeSet 455
Or}       Proprietary <Prtry> [1..1] Text 457
     AccountOwner <AcctOwnr> [0..1] ± 457
     AccountIdentification <AcctId> [0..1] ± 458
Or}   AllCurrentLimits <AllCurLmts> [1..1]  458
     SystemIdentification <SysId> [0..1] ± 459
     Type <Tp> [1..1]  459
{Or       Code <Cd> [1..1] CodeSet 459
Or}       Proprietary <Prtry> [1..1] Text 461
     AccountOwner <AcctOwnr> [0..1] ± 461
     AccountIdentification <AcctId> [0..1] ± 462
11.4.2.1  CurrentLimitIdentification <CurLmtId>
Presence: [1..1]
Definition: Identification of the current limit.
Impacted by: C2 "BilateralLimitCounterparty1Rule", C3 "BilateralLimitCounterparty2Rule"
CurrentLimitIdentification <CurLmtId> contains the following LimitIdentification8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SystemIdentification <SysId> [0..1] ± 454
   BilateralLimitCounterpartyIdentification
<BilLmtCtrPtyId>
[0..1] ± 454
   Type <Tp> [1..1]  455
{Or     Code <Cd> [1..1] CodeSet 455
Or}     Proprietary <Prtry> [1..1] Text 457
   AccountOwner <AcctOwnr> [0..1] ± 457
   AccountIdentification <AcctId> [0..1] ± 458
Approved by the Payments SEG on 04 February 2025 camt.012.001.08 DeleteLimitV08
Cash Management - Maintenance 2024 - 2025 453 February 2025
```

