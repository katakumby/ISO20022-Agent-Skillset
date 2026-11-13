---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["10 camt.011.001.08 ModifyLimitV08", "10.4 Message Building Blocks", "10.4.2 LimitDetails <LmtDtls>", "10.4.2.1 LimitIdentification <LmtId>", "10.4.2.1.2 Default <Dflt>", "10.4.2.1.2.1 SystemIdentification <SysId>"]
file_pages: [434]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.011.001.08"]
---

# 10.4.2.1.2.1 SystemIdentification <SysId>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 434 to 434.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 434

```text
Default <Dflt> contains the following LimitIdentification8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SystemIdentification <SysId> [0..1] ± 434
   BilateralLimitCounterpartyIdentification
<BilLmtCtrPtyId>
[0..1] ± 434
   Type <Tp> [1..1]  435
{Or     Code <Cd> [1..1] CodeSet 435
Or}     Proprietary <Prtry> [1..1] Text 437
   AccountOwner <AcctOwnr> [0..1] ± 437
   AccountIdentification <AcctId> [0..1] ± 438
Constraints
• BilateralLimitCounterparty1Rule
If Type is MULT, then BilateralLimitCounterpartyIdentification is not allowed.
On Condition
    /Type/Code is equal to value 'Multilateral'
Following Must be True
    /BilateralLimitCounterpartyIdentification Must be absent
• BilateralLimitCounterparty2Rule
If Type is BILI or NELI or INBI, then BilateralLimitCounterpartyIdentification must be present.
On Condition
    /Type/Code is equal to value 'Bilateral'
 Or    /Type/Code is equal to value 'NetBilateral'
 Or    /Type/Code is equal to value 'IndirectBilateral'
Following Must be True
    /BilateralLimitCounterpartyIdentification Must be present
10.4.2.1.2.1  SystemIdentification <SysId>
Presence: [0..1]
Definition: Identification of a particular cash clearing system.
SystemIdentification <SysId> contains one of the following elements (see
"SystemIdentification2Choice" on page 846 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketInfrastructureIdentification <MktInfrstrctrId> [1..1] ± 846
Or}   Country <Ctry> [1..1] CodeSet C3 846
10.4.2.1.2.2  BilateralLimitCounterpartyIdentification <BilLmtCtrPtyId>
Presence: [0..1]
Definition: Identification of the system member for which the limit is established.
Approved by the Payments SEG on 04 February 2025 camt.011.001.08 ModifyLimitV08
Cash Management - Maintenance 2024 - 2025 434 February 2025
```

