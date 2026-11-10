---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["39 reda.019.001.01 SecuritiesAccountQueryV01", "39.4 Message Building Blocks", "39.4.2 SearchCriteria <SchCrit>"]
file_pages: [2109]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.019.001.01"]
---

# 39.4.2 SearchCriteria <SchCrit>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2109 to 2109.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2109

```text
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader2" on page 3007 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 3007
   CreationDateTime <CreDtTm> [0..1] DateTime 3008
   RequestType <ReqTp> [0..1]  3008
{Or     PaymentControl <PmtCtrl> [1..1] CodeSet 3008
Or     Enquiry <Enqry> [1..1] CodeSet 3008
Or}     Proprietary <Prtry> [1..1] ± 3009
39.4.2 SearchCriteria <SchCrit>
Presence: [1..1]
Definition: Defines the criteria to be used to query the securities account reference data by the
executing system.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.019.001.01 SecuritiesAccountQueryV01
Target2-Securities 2109 August 2026
```

