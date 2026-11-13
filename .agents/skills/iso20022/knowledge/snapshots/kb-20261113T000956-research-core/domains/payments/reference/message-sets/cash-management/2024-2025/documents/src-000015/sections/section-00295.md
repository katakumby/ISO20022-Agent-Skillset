---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["10 camt.011.001.08 ModifyLimitV08", "10.4 Message Building Blocks", "10.4.2 LimitDetails <LmtDtls>", "10.4.2.1 LimitIdentification <LmtId>"]
file_pages: [427, 428]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.011.001.08"]
---

# 10.4.2.1 LimitIdentification <LmtId>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 427 to 428.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 427

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       AccountIdentification <AcctId> [0..1] ± 446
   NewLimitValueSet <NewLmtValSet> [1..1]  446
     StartDateTime <StartDtTm> [0..1] ± 447
     Amount <Amt> [1..1] ± 447
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 447
   OldLimitValueSet <OdLmtValSet> [0..1]  447
     Amount <Amt> [1..1] ± 447
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 448
   LimitValueAmendment <LmtValAmdmnt> [0..1]  448
{Or     IncreaseAmount <IncrAmt> [1..1] ± 448
Or}     DecreaseAmount <DcrAmt> [1..1] ± 448
Constraints
• OldLimitOrLimitAmendmentPresenceRule
OldLimitValueSet or LimitValueAmendment must be absent, both can be absent.
Following Must be True
    /OldLimitValueSet Must be absent
 Or    /LimitValueAmendment Must be absent
10.4.2.1  LimitIdentification <LmtId>
Presence: [1..1]
Definition: Identification of the default limit.
Approved by the Payments SEG on 04 February 2025 camt.011.001.08 ModifyLimitV08
Cash Management - Maintenance 2024 - 2025 427 February 2025
```

## File page 428

```text
LimitIdentification <LmtId> contains one of the following LimitIdentification3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Current <Cur> [1..1]  C3, C4 429
     SystemIdentification <SysId> [0..1] ± 429
     BilateralLimitCounterpartyIdentification
<BilLmtCtrPtyId>
[0..1] ± 430
     Type <Tp> [1..1]  430
{Or       Code <Cd> [1..1] CodeSet 430
Or}       Proprietary <Prtry> [1..1] Text 432
     AccountOwner <AcctOwnr> [0..1] ± 432
     AccountIdentification <AcctId> [0..1] ± 433
Or   Default <Dflt> [1..1]  C3, C4 433
     SystemIdentification <SysId> [0..1] ± 434
     BilateralLimitCounterpartyIdentification
<BilLmtCtrPtyId>
[0..1] ± 434
     Type <Tp> [1..1]  435
{Or       Code <Cd> [1..1] CodeSet 435
Or}       Proprietary <Prtry> [1..1] Text 437
     AccountOwner <AcctOwnr> [0..1] ± 437
     AccountIdentification <AcctId> [0..1] ± 438
Or   AllCurrent <AllCur> [1..1]  438
     SystemIdentification <SysId> [0..1] ± 439
     Type <Tp> [1..1]  439
{Or       Code <Cd> [1..1] CodeSet 439
Or}       Proprietary <Prtry> [1..1] Text 441
     AccountOwner <AcctOwnr> [0..1] ± 441
     AccountIdentification <AcctId> [0..1] ± 442
Or}   AllDefault <AllDflt> [1..1]  442
     SystemIdentification <SysId> [0..1] ± 443
     Type <Tp> [1..1]  443
{Or       Code <Cd> [1..1] CodeSet 443
Or}       Proprietary <Prtry> [1..1] Text 445
     AccountOwner <AcctOwnr> [0..1] ± 445
     AccountIdentification <AcctId> [0..1] ± 446
Approved by the Payments SEG on 04 February 2025 camt.011.001.08 ModifyLimitV08
Cash Management - Maintenance 2024 - 2025 428 February 2025
```

